from fastapi import FastAPI

app = FastAPI(title="FastAPI, Docker, and CookieCuttin")


@app.get("/")
def read_root():
    return {"hello": "world"}