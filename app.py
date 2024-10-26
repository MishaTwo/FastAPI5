from fastapi import FastAPI


app = FastAPI()

tasks = dict()

@app.get('/return/')
def return_all():
    return tasks

@app.get('/return/{id}')
def return_task(id:int):
    return tasks[id]
    
@app.post('/return/create_post/{id}')
def create_post(id:int, task:str):
    tasks[id] = task
    return tasks[id]

@app.delete('/return/delete/{id}')
def delete(id:int):
    tasks.pop(id)
    return "Все успішно видаленно!", tasks
    

@app.patch('/return/update/{id}')
def update_task(id:int, updated_task:str):
    tasks[id] = updated_task
    return "Все оновленно!", tasks 