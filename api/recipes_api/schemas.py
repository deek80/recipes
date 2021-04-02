from typing import List
from pydantic import BaseModel


class Schema(BaseModel):
    class Config:
        orm_mode = True


class Ingredient(Schema):
    id: int
    name: str


class Requirement(Schema):
    ingredient: Ingredient
    amount: str


class Product(Schema):
    ingredient: Ingredient
    amount: str


class Instruction(Schema):
    id: str
    details: str
    duration: int
    requirements: List[Requirement]
    products: List[Product]


class Recipe(Schema):
    name: str
    path: str
    instructions: List[Instruction]
