from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rarity = Column(Enum('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'), nullable=False)
    image_url = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    inventory = relationship('Inventory', back_populates='user')

class Pack(Base):
    __tablename__ = 'packs'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cards = relationship('Card', secondary='pack_cards')

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='inventory')
    cards = relationship('Card')

class Marketplace(Base):
    __tablename__ = 'marketplace'
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey('cards.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    price = Column(Integer, nullable=False)

class WorkAssignment(Base):
    __tablename__ = 'work_assignments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String, nullable=False)
    due_date = Column(DateTime)

class Badge(Base):
    __tablename__ = 'badges'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(DateTime)

class Community(Base):
    __tablename__ = 'communities'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    card_id = Column(Integer, ForeignKey('cards.id'), nullable=False)

class Leaderboard(Base):
    __tablename__ = 'leaderboards'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rank = Column(Integer, nullable=False)

