"""
How about this: 
Ingredient --many-to-one--> Instruction --one-to-many--> Ingredient

Instructions have inputs and outputs, and server as a way to get from one ingredient
to another. i.e.
    Ingredients required:
        onion
        mushrooms

    Instruction:
        dice {onion} and {mushroom} and fry in oil until tender

    Ingredients produced:
        onion-mushroom-mixture

and then in a later instruction you'll use that mixture to complete whatever thing
you're cooking. I think I should support unnamed products somehow, so you don't have
to overdo it for sequential instructions (Cook the thing for 5 minutes, add this and
cook for another 2 minutes, add that and cook for 30 more seconds, etc). Or maybe a
better way would be to have it really easy to name the intermediate mixtures...
For baking you see "dry ingredients" and whatnot. "Pan sauce", etc...I guess you could
push the same name down the line if you just augmented it a bunch of times.

I'd also like to support non-food "ingredients" and 0-requirement instructions like:
    Instruction(preheat the oven to 425F) --> Ingredient(preheated oven)

I can't think of a word that's the right level of generic, other than ingredient. Like
a fucking oven isn't an ingredient, but I don't want the model to be called Thing etiher.
"""

__all__ = ["Model", "Ingredient", "Instruction"]

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import as_declarative, declared_attr, relationship


@as_declarative()
class Model:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)


requirements = Table(
    "requirements",
    Model.metadata,
    Column("ingredient", Integer, ForeignKey("ingredient.id")),
    Column("instruction", Integer, ForeignKey("instruction.id")),
    Column("amount", String),
)

products = Table(
    "products",
    Model.metadata,
    Column("instruction", Integer, ForeignKey("instruction.id")),
    Column("ingredient", Integer, ForeignKey("ingredient.id")),
)


class Ingredient(Model):
    name = Column(String, unique=True, index=True)

    # every "recipe" Ingredient will have Instructions
    instructions = relationship("Instruction", back_populates="recipe")


class Instruction(Model):
    details = Column(String)
    duration_seconds = Column(Integer, default=0)

    # every Instruction will belong to a "recipe" Ingredient
    recipe_id = Column(Integer, ForeignKey("ingredient.id"))
    recipe = relationship("Ingredient", back_populates="instructions")

    # Instructions can have many requirements and products
    requirements = relationship("Ingredient", secondary=requirements)
    products = relationship("Ingredient", secondary=products)
