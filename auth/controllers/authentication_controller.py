from auth.schemas.register_schema import RegisterInput
from user.repositories.user_repository import UserRepository
from fastapi import HTTPException

from sqlalchemy.orm import Session
from fastapi import Depends

class AuthenticationController:

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(self, schema: RegisterInput):
        try:
            username = self.user_repository.get_user_by_email(schema.username)
            if username:
                raise HTTPException(status_code=400, detail='User already exists')
            email = self.user_repository.get_user_by_email(schema.email)
            if email:
                raise HTTPException(status_code=400, detail='Email already exists')
            user = self.user_repository.create_user(schema)
            return {"username":user.username, "email": user.email}
        except Exception as e:
            raise e