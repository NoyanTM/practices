import base64
import json

import jwt
import httpx
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR
from pydantic import BaseModel

from backend.config import config

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{config.KEYCLOAK_BASE_URL}/realms/{config.KEYCLOAK_REALM}/protocol/openid-connect/auth",
    tokenUrl=f"{config.KEYCLOAK_BASE_URL}/realms/{config.KEYCLOAK_REALM}/protocol/openid-connect/token",
    auto_error=False
)

class Token(BaseModel):
    username: str
    roles: list[str]


# @TODO: validate all possible fields of JWT:
# issuer, audience, etc. via pyjwt options
def validate_token(token: str) -> Token:
    "Verification and validation of JWT token"

    try:
        oidc_server = f"{config.KEYCLOAK_BASE_URL}/realms/{config.KEYCLOAK_REALM}"
        oidc_config = httpx.get(f"{oidc_server}/.well-known/openid-configuration")
        oidc_config.raise_for_status()
        oidc_config = oidc_config.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=f"OIDC provider is not available")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Incorrect format of response from OIDC provider")
    
    signing_algorithms = oidc_config["id_token_signing_alg_values_supported"]
    jwks_client = jwt.PyJWKClient(oidc_config["jwks_uri"])
    
    try:
        unverified_header = jwt.get_unverified_header(token)
    except jwt.PyJWKError as e:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail=f"Invalid header")
    kid = unverified_header.get("kid", "")
    if not kid:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail=f"Empty or missing kid")
    # @TODO: validate for kid
    # key_data = next((key for key in jwks["keys"] if key["kid"] == kid), None)
    # if not key_data: raise Matching key not found in JWKS
    
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token).key # id_token = token["id_token"]
    except jwt.PyJWKClientError as e:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Public key is not valid")
    try:
        decoded_data = jwt.decode_complete(
            token, # id_token
            key=signing_key,
            audience=config.KEYCLOAK_CLIENT_ID,
            algorithms=signing_algorithms,
            options={
                "verify_aud": False
            }
        )
    except jwt.PyJWKError as e:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {e}")
    # @TODO: https://pyjwt.readthedocs.io/en/stable/usage.html#oidc-login-flow
    
    # @TODO: validate if empty, missing required claims
    payload = decoded_data.get("payload")
    roles = payload.get("realm_access").get("roles")
    username = payload.get("preferred_username")
    return Token(username=username, roles=roles)

def get_current_user(token: str = Depends(oauth2_scheme)):
    print(token)
    if not token:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    validated_token = validate_token(token)
    # try except Exception as e: raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Token invalid")
    return validated_token

def require_roles(*allowed_roles: str):
    def _dependency(token: Token = Depends(get_current_user)) -> Token:
        roles = token.roles
        if not any(role in roles for role in allowed_roles):
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Insufficient permissions or role")
        # return token_data
    return _dependency
