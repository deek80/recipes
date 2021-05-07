from recipes_api.models import *


def seed_db(session):
    # It's pretty fucked up to create a recipe this way...but I'm still holding
    # onto the idea that it makes sense in the end. Hopefully it won't be too
    # hard to automate this creation, given a representation of a recipe from
    # the front end.
    Model.metadata.create_all(bind=session.get_bind())
    recipe = Recipe(data={"name": "Sorta Shepherd's Pie", "path": "test-recipe"})
    session.add(recipe)

    mash = Instruction(
        recipe=recipe,
        data={
            "required": {
                "ingredients": [
                    {"name": "potatoes", "amount": "3 large"},
                    {"name": "butter", "amount": "1 tbsp"},
                ],
            },
            "details": "dice, boil, and drain {{ingredients.0}}. Mash with {{ingredients.1}}.",
        },
    )
    session.add(mash)

    beef = Instruction(
        recipe=recipe,
        data={
            "required": {
                "ingredients": [
                    {"name": "ground beef", "amount": "450g"},
                    {"name": "frozen peas and carrots", "amount": "200g"},
                ]
            },
            "details": "brown the {{ingredients.0}} in a frying pan (about 5 minutes) then mix in {{ingredients.1}} and cook for another 3 minutes.",
        },
    )
    session.add(beef)
    session.flush()  # requried for ids below

    mixture = Instruction(
        recipe=recipe,
        data={
            "required": {
                "ingredients": [
                    {"name": "butter", "amount": "2 tbsp"},
                ],
                "instructions": [
                    {"id": mash.id, "name": "mashed potatoes", "amount": "all"},
                    {"id": beef.id, "name": "ground beef mixture", "amount": "all"},
                ],
            },
            "details": "spread the {{instructions.1}} in a 9x13 glass baking dish, and spread the {{instructions.0}} evenly on top. Sprinkle the {{ingredients.0}} in 2 or 3 chunks on top, and bake for 30 minutes",
        },
    )
    session.add(mixture)
    session.commit()
