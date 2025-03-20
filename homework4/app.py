from fastapi import FastAPI, APIRouter, HTTPException, Request, Depends, Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from data import Cake, items
import uuid

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

api_router = APIRouter(prefix='/api', tags=['API'])


@api_router.get('/items', response_model=List[Cake])
def get_items():
    """
    Get all cake items
    """
    return items


@api_router.get('/items/{item_id}', response_model=Cake)
def get_item(item_id: str = Path(...)):
    """
    Find cake item with its ID
    """
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail='Cake not found')


@api_router.post('/items', response_model=Cake)
def create_item(item: Cake):
    """
    Create new cake item
    """
    if item.id is None:
        item.id = str(uuid.uuid4())
    items.append(item)
    return item


app.include_router(api_router)


@app.get('/')
def index(request: Request, products: List[Cake] = Depends(get_items)):
    return templates.TemplateResponse('index.html', {'request': request, 'products': products})


@app.get('/about/')
def about(request: Request):
    return templates.TemplateResponse('about.html', {'request': request})


@app.get('/{cake_id}')
def cake_detail(request: Request, cake_id: str = Path(...)):
    cake = get_item(item_id=cake_id)
    return templates.TemplateResponse('cake_detail.html', {'request': request, 'cake': cake})
