"""
How about this: 
  Food ---> Instruction ---> Food

  Instructions have 0 or more (1 or more?) required foods, and produce 1 or more foods?

  hmm, how about instructions like "turn the oven to 425"...do we even want stuff like that?
  maybe I don't give a shit about things like that. just have an instruction like
  "bake the thing at 425 for 20 minutes" with a product of "baked thing"


  I suppose I could loosen the names here to like "item" and "instruction" and then
  "preheated oven" could be a product. Also instructions could then have 0 requirements
  and 1 or more products. Anyway, I kinda like thinking about this hah
"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship

Model = declarative_base()

requirements = Table(
    "requirements",
    Model.metadata,
    Column("ingredient", Integer, ForeignKey("ingredient.id")),
    Column("instruction", Integer, ForeignKey("instruction.id")),
)

products = Table(
    "products",
    Model.metadata,
    Column("instruction", Integer, ForeignKey("instruction.id")),
    Column("ingredient", Integer, ForeignKey("ingredient.id")),
)


class Ingredient(Model):
    __tablename__ = "ingredient"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Instruction(Model):
    __tablename__ = "instruction"

    id = Column(Integer, primary_key=True, index=True)
    details = Column(String)

    requirements = relationship("Ingredient", secondary=requirements)
    products = relationship("Ingredient", secondary=products)
