from fastapi import FastAPI
from pydantic  import BaseModel

app = FastAPI()

class student(BaseModel):
    name: str
    sex : str

@app.get('/')
def index():
    return {"name":"davit"}

