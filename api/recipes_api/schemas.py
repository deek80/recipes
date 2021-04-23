from typing import List
from pydantic import BaseModel


class Schema(BaseModel):
    class Config:
        orm_mode = True


class Instruction(Schema):
    id: int
    data: dict


class Recipe(Schema):
    id: int
    data: dict
    instructions: List[Instruction]
