from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, index=True) 
    profession = Column(String)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    money = Column(Integer, default=0)
    energy = Column(Integer, default=100)
    strength = Column(Integer, default=1)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    strength_bonus = Column(Integer, default=0)
    description = Column(String)
    value = Column(Integer)
    character_id = Column(Integer, ForeignKey("characters.id"))

    owner = relationship("Character", back_populates="items")