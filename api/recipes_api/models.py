"""
Trying a new data setup. Half way through the POC I already hate
how hard it is to query and create these things.

So, I'm going to try the suggestion from a halihax chat. Basically
put your keys and table relationships in SQL format, and the data itself
in a json column.

ok how about this
  Recipe:
    id
    data

  Instruction:
    id
    recipe_id
    data: {
        required_ingredients: [
            {name: "things", amount: "2 cups"},
        ],
        required_instructions: [
            {id: 234, name: "stuff", amount: "all"}
        ],
    }
"""

__all__ = ["Instruction", "Model", "Recipe"]

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import as_declarative, declared_attr, relationship


@as_declarative()
class Model:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class Recipe(Model):
    id = Column(Integer, primary_key=True)
    data = Column(JSONB)

    instructions = relationship("Instruction", back_populates="recipe")


class Instruction(Model):
    id = Column(Integer, primary_key=True)
    data = Column(JSONB)

    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    recipe = relationship("Recipe", back_populates="instructions")
