
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///db.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class User_Game(Base):
    __tablename__ = 'users_games'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="users_games")
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Game", back_populates="users_games")

class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Game", back_populates="prices")
    price = Column(Integer)
    platform_id = Column(Integer, ForeignKey('platforms.id'))
    platform = relationship("Platform", back_populates="prices")

class Platform(Base):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


Base.metadata.create_all(engine)
