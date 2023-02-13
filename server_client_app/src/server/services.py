import hashlib

from sqlalchemy.orm import Session

import models
import schemas


class UserService:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: schemas.UserCreate) -> models.User:
        hashed_password = self._hash_password(user.password)
        db_user = models.User(login=user.login, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_login(self, login: str) -> models.User | None:
        return self.db.query(models.User).filter(models.User.login == login).first()

    def _hash_password(self, raw_password: str) -> str:
        return hashlib.md5(raw_password.encode('utf-8')).hexdigest()
