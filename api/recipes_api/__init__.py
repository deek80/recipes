from fastapi import FastAPI
from recipes_api.setup import config
from recipes_api.views import recipes, test

app = FastAPI()
app.include_router(recipes)
if config.environment == "test":
    app.include_router(test)
