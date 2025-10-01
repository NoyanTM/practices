import os
from dataclasses import dataclass, fields
from typing import Self


@dataclass
class Config:
    KEYCLOAK_BASE_URL: str
    KEYCLOAK_REALM: str
    KEYCLOAK_CLIENT_ID: str
    KEYCLOAK_OPENID_URL: str

    @classmethod
    def from_env(cls) -> Self:
        config = {
            field.name: os.environ.get(field.name, None)
            for field in fields(cls)
        }
        config["KEYCLOAK_OPENID_URL"] = f"{config["KEYCLOAK_BASE_URL"]}/realms/{config["KEYCLOAK_REALM"]}/protocol/openid-connect/certs"
        print(config) # debug
        return cls(**config)

config = Config.from_env()