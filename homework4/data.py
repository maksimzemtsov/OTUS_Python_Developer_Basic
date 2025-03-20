from pydantic import BaseModel


class Cake(BaseModel):
    id: str = None
    name: str
    description: str
    image: str


items = [
    Cake(
        id='b7e6b36c-5d2f-4c07-88e9-b72fa67f3fcd',
        name='Эчпочмак',
        description='Татарский пирожок с картошкой и мясом',
        image="https://avatanplus.com/files/resources/original/5ac034364be381627ecbf427.png"
    ),
    Cake(
        id='c8d7c47a-9f3d-4a8a-98e5-fdbe80e2d1a3',
        name='Курник',
        description='Пирожок с мясом и картошкой',
        image="https://nyamkin.ru/images/recepts/medium/5e508220990d4.jpg"
    ),
    Cake(
        id='a2b4c6d8-1e3f-4g5h-6i7j-8k9l0m1n2o3p',
        name='Беляш',
        description='Жареный пирожок с мясом',
        image="https://ekathleb.ru/upload/iblock/09e/09edef59c505760dda2003b89c0190c6.jpg"
    ),
]
