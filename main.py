from fastapi import FastAPI
from routers import task, user
from models import User
from models.user import table
from models.task import tableT
import sqlite3
app = FastAPI()

connection = sqlite3.connect('taskmanager.db')
cursor = connection.cursor()
def cr_db():
    cursor.execute(f'{table}')
    cursor.execute(f'{tableT}')
    connection.commit()
cr_db()
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)
