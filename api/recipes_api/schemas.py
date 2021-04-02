from typing import List
from pydantic import BaseModel


class ModelSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True


class IngredientSchema(ModelSchema):
    name: str


class InstructionSchema(ModelSchema):
    details: str
    duration: int
    requirements: List[IngredientSchema]
    products: List[IngredientSchema]


class RecipeSchema(ModelSchema):
    name: str
    path: str
    instructions: List[InstructionSchema]