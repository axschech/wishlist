
import os

from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, Float
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
    email = Column(String, unique=True)
    password = Column(String)
    steam_id = Column(Integer, unique=True)
    humble_id = Column(Integer, unique=True)
    last_refresh = Column(DateTime)
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
    price = Column(Float(default=0, precision=23))
    discount = Column(Float(default=0, precision=23))
    def original(self):
        try :
            original = int(self.price / (1 - self.discount))
        except ZeroDivisionError:
            original = self.price
        return original

    platform_id = Column(Integer, ForeignKey('platforms.id'))
    platform = relationship("Platform")

class Platform(Base):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

Base.metadata.create_all(engine)

# print "\nSeeding\n"
# Session = sessionmaker(bind=engine)

# session = Session()

# games = [
#     Game(name="A Game", price=Price(price=20.00, discount=0.20, platform=Platform(name="Steam")))
# ]
# user = User(name="Alex", password="words", email="ax.schech@gmail.com", games=games, steam_id=76561197968229753)
# session.add(user)
# session.commit()

# for game in session.query(Game).all():
#     print game.price.price
#     print game.price.discount
#     print game.price.original()
