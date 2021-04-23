from recipes_api.models import *


def init_db(session):
    Model.metadata.create_all(bind=session.get_bind())


def fake_recipe() -> Recipe:
    return Recipe(
        instructions=[
            Instruction(data={"hello": "world"}),
            Instruction(data={"instruction": 2}),
        ],
        data={"my recipe": "data", "nested": {"stuff": "is ok"}},
    )


def seed_db(session):
    session.add(fake_recipe())
    session.commit()
