from .connection import engine
from .models import Ingredient, Instruction, Recipe, Model


def init_db(session):
    Model.metadata.create_all(bind=session.get_bind())


def seed_db(session):
    start = [Ingredient(name=f"start {i}") for i in range(10)]
    middle = [Ingredient(name=f"mid {i}") for i in range(3)]
    end = Ingredient(name="end")

    recipe = Recipe(
        name="recipe name",
        path="recipe-url-path",
        instructions=[
            Instruction(
                details="the first thing",
                requirements=start[:4],
                products=[middle[0]],
            ),
            Instruction(
                details="the second thing",
                requirements=start[4:7],
                products=[middle[1]],
            ),
            Instruction(
                details="the third thing",
                requirements=start[7:9],
                products=[middle[2]],
            ),
            Instruction(
                details="the last thing",
                requirements=[start[9], *middle],
                products=[end],
            ),
        ],
    )
    session.add(recipe)
    session.commit()
