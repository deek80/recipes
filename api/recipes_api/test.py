from recipes_api.models import *


def init_db(session):
    Model.metadata.create_all(bind=session.get_bind())


def fake_recipe() -> Recipe:
    i0 = Instruction(
        details="instruction #0",
        requirements=[
            Requirement(ingredient=Ingredient(name="req 0"), amount="a pinch"),
            Requirement(ingredient=Ingredient(name="req 1"), amount="1 tsp"),
            Requirement(ingredient=Ingredient(name="req 2"), amount="2 cups"),
        ],
        products=[
            Product(ingredient=Ingredient(name="prod i0[0]")),
            Product(ingredient=Ingredient(name="prod i0[1]")),
        ],
    )

    i1 = Instruction(
        details="instruction #1",
        requirements=[
            Requirement(ingredient=Ingredient(name="req 3"), amount="a bunch"),
            Requirement(ingredient=i0.products[0].ingredient, amount="_all"),
        ],
        products=[Product(ingredient=Ingredient(name="prod i1"))],
    )

    i2 = Instruction(
        details="instruction #2",
        requirements=[
            Requirement(ingredient=i0.products[1].ingredient, amount="_all"),
            Requirement(ingredient=i1.products[0].ingredient, amount="_all"),
        ],
        products=[Product(ingredient=Ingredient(name="Final"))],
    )

    return Recipe(name="recipe name", path="recipe-url-path", instructions=[i0, i1, i2])


def seed_db(session):
    session.add(fake_recipe())
    session.commit()
