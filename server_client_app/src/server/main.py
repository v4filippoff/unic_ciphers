from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

import schemas
from db import get_db_session, init_db
from services import UserService

app = FastAPI()
app.mount('/static', StaticFiles(directory='../client/static', html=True), name='static')
templates = Jinja2Templates(directory='../client/templates')


@app.on_event('startup')
def on_startup():
    init_db()


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("registration.html", {'request': request})


@app.post('/api/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_login(user.login)
    if db_user:
        raise HTTPException(status_code=400, detail='Такой пользователь уже существует.')
    return user_service.create_user(user)
