from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Model = declarative_base()


class Recipe(Model):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)

    steps = relationship("Step", back_populates="recipe")


class Step(Model):
    __tablename__ = "step"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)

    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    recipe = relationship("Recipe", back_populates="steps")


class Ingredient(Model):
    __tablename__ = "ingredient"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)