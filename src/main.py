from fastapi import FastAPI

app = FastAPI(title='URL Shortener')

@app.get('/')
def get_default():
    return {'status': 'OK'}

@app.get('/users/user/{name}')
def get_user(name: str, age: int = 18):
    return {'code': 200, 'name': name, 'age': age}