# @TODO: keycloak to be as Middleware
# @TODO: application factory
# @TODO: change systemexit to logging
# @TODO: instead of depends use decorators or can_

import uvicorn
from fastapi import FastAPI

from backend.routers import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=router)
    return app


def main() -> None:
    uvicorn.run(create_app)


if __name__ == "__main__":
    main()