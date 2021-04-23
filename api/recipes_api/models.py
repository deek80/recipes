"""
Trying a new data setup. Half way through the POC I already hate
how hard it is to query and create these things.

So, I'm going to try the suggestion from a halihax chat. Basically
put your keys and table relationships in SQL format, and the data itself
in a json column.

Hmm, I forget how this was much different than what I've got. I know I
had something decent in mind.


ok, what things should be easy to do:
- must: list the recipes
- should: filter the recipes by name
- must: list the ingredients/amounts for a recipe
- should: list the recipes containing all of these ingredients
- must: what instructions can be done next
- must: create/update a recipe
- maybe: rate/comment a recipe?

ok how about this
  Recipe:
    name, etc

  Instruction:
    details, etc
    recipe_id

    data: {
        required_ingredients: [
            {id: 123, amount: "2 cups"},
        ],
        required_instructions: [
            {id: 234, product: "stuff", amount: "all"}
        ],
        products: ["stuff", "etc"]
    }

  Ingredient:
    name, etc

pros:
  easy to list recipes
  easy to get edges from graph without crazy joins

cons:
  somewhat annoying to get all ingredients for a recipe, but you'd do
  that in the backend...so it's not so bad.
    1. get instructions where recipe_id = blah
    2. get ingredients where id in (instructions.required_ingredients.id list)

thoughts:
  jeez, maybe Ingredient doesn't deserve to be a class at this point. you could still
  build a list of all ingredients if need be, or search it. postgres is pretty damn
  good with json columns.


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
