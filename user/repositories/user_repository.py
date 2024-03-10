from user.models.user_model import User
import bcrypt

class UserRepository:

    def __init__(self, db):
        self.db = db

    def create_user(self, user_data):
        try:
            password = user_data.password.encode('utf-8')
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            hashed_password = hashed.decode('utf-8')

            user_data_dict = user_data.dict()
            user_data_dict['password'] = hashed_password

            user = User(**user_data_dict)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def get_user_by_username(self, username: str):
        try:
            return self.db.query(User).filter(User.username == username).first()
        except Exception as e:
            raise e

    def get_user_by_email(self, email: str):
        try:
            return self.db.query(User).filter(User.email == email).first()
        except Exception as e:
            raise e
        
    def get_user_by_id(self, id: int):
        try:
            return self.db.query(User).filter(User.id == id).first()
        except Exception as e:
            raise e
        
    def get_all_users(self):
        try:
            return self.db.query(User).all()
        except Exception as e:  
            raise e