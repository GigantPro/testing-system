from .base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, Date


__all__ = ("User", "SessionToken")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    login = Column(String)
    img_url = Column(String)
    passhash = Column(String)
    
    def __init__(self, id, name, surname, login, img_url, passhash) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self,login = login
        self.img_url = img_url
        self.passhash = passhash
    
    def __repr__(self):
        return (
            f"<User(id='{self.id}',"
            f"surname='{self.surname}',"
            f"login='{self.login}',"
            f"passhash='{self.passhash}',"
            f"passhash='{self.passhash}')>"
        )


class SessionToken(Base):
    __tablename__ = "session_tokens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String)
    user_id = ForeignKey('users.id')
    created_date = Column(Date, autoincrement=True)
    
    def __init__(self, id, token, user_id, created_date) -> None:
        self.id = id
        self.token = token
        self.user_id = user_id
        self.created_date = created_date
    
    def __repr__(self) -> str:
        return (
            f"<SessionToken(id='{self.id}',"
            f"token='{self.token}',"
            f"user_id='{self.user_id}',"
            f"created_date='{self.created_date}')>"
        )
