from fastapi import FastAPI
from .settings.database import engine, authentication
from .settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from .testapp.router import app_myapp
from .settings.auth.routers import role_router,user_router
from .settings.auth.configs import authentication_router
app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
app.include_router(app_myapp)
app.include_router(user_router)
app.include_router(authentication_router)
app.include_router(role_router)
app.add_middleware(
    ErrorHandlingMiddleware,
)

