from fastapi import FastAPI
from auth.routes.authentication_routes import auth_router

app = FastAPI()

app.include_router(auth_router, prefix='/auth', tags=['auth'])