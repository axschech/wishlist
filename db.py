
import os

from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

try:
    os.remove('db.db')
except OSError:
    pass

engine = create_engine('sqlite:///db.db', echo=True)
Base = declarative_base()

print "\Schema\n"

association_table = Table('users_games', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('game_id', Integer, ForeignKey('games.id'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    games = relationship('Game', secondary=association_table, backref="games")

    # def __repr__(self):
    #    return "<User(name='%s', name='%s', password='%s')>" % (
    #                         self.name, self.name, self.password)
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price_id = Column(Integer, ForeignKey('prices.id'))
    price = relationship("Price")

class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    platform_id = Column(Integer, ForeignKey('platforms.id'))
    platform = relationship("Platform")

class Platform(Base):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


Base.metadata.create_all(engine)

print "\nSeeding\n"
Session = sessionmaker(bind=engine)

session = Session()

games = [
    Game(name="A Game", price=Price(price="150", platform=Platform(name="Steam")))
]
user = User(name="Alex", password="words", email="ax.schech@gmail.com", games=games)
session.add(user)
session.commit()

for instance in session.query(User).all():
    for game in instance.games:
        print game.name
