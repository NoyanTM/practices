# practice-4

## Description
1. Setup Python
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
source .env
```

2. Generate client for "/admin" endpoint (optional)
```
curl -O -L https://www.keycloak.org/docs-api/latest/rest-api/openapi.yaml
openapi-generator-cli generate -g python -o keycloak-generated-client -i openapi.yaml
cd ./keycloak-generated-admin-client
python3 -m build --wheel
pip install ./dist/openapi_client-1.0.0-py3-none-any.whl
```

3. Setup Keycloak in Docker
```
make setup
```

4. Setup resource server API
```
python3 -m backend.main
```