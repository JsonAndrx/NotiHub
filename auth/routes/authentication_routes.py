from fastapi import APIRouter, Depends
from auth.controllers.authentication_controller import AuthenticationController
from auth.schemas.register_schema import RegisterInput, RegisterOutput

from config.database.connect_db import get_db
from sqlalchemy.orm import Session


auth_router = APIRouter()

def get_auth_service():
    return AuthenticationController()

@auth_router.post('/register', response_model=RegisterOutput, status_code=201)
def auth_register(user: RegisterInput, db: Session = Depends(get_db)):
    auth_service = AuthenticationController(db)
    return auth_service.register(user)