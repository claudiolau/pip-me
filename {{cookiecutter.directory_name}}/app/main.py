from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_welcome():
    return {"Hello": "{{cookiecutter.greeting_recipient}}"}