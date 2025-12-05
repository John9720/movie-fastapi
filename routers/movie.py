from typing import Optional
from fastapi import Path, Query, Request, HTTPException, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from pydantic import BaseModel, Field
from user_jwt import validateToken
from db.database import Session
from models.movies import Movie as ModelMovie

routerMovie = APIRouter()



class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        if data['email'] != 'string@outlook.com':
            raise HTTPException(status_code=403, detail='Credenciales incorrectas')

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default = "Título de la película", min_length = 3, max_length=50)
    overview: str = Field(default = "Descripción de la película", min_length = 3, max_length=100)
    year: int = Field(default = 2025)
    rating: float = Field(ge = 1, le = 10)
    category: str = Field(default = "Aquí va la categoría", min_length = 3, max_length=40)



@routerMovie.get("/movies", tags=["Movies"], dependencies=[Depends(BearerJWT())])
def get_movies():
    db = Session()
    data = db.query(ModelMovie).all()
    return JSONResponse(content=jsonable_encoder(data))

@routerMovie.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int = Path(ge=1, le=100)):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'Película no encontrada'})
    return JSONResponse(content=jsonable_encoder(data))

@routerMovie.get("/movies/", tags=['Movies'])
def get_movies_by_category(category: str = Query(min_length=3, max_length=50)):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.category == category).all()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'Categoría no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))



@routerMovie.post("/movies/", tags=['Movies'], status_code=201)
def create_movie(movie: Movie):
    db = Session()
    newMovie = ModelMovie(**movie.model_dump())
    db.add(newMovie)
    db.commit()
    return JSONResponse(content={"message": "Se ha cargado una nueva película", "movie": movie.model_dump()})

@routerMovie.put("/movies/{id}", tags=["Movies"])
def update_movie(movie: Movie):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == movie.id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'No se encontró la película'})
    data.title = movie.title
    data.overview = movie.overview
    data.year = movie.year
    data.rating = movie.rating
    data.category = movie.category
    db.commit()
    return JSONResponse(content={"message": "La película se ha modificado"})

@routerMovie.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={"message": "No se encontró la película a borrar"})
    db.delete(data)
    db.commit()
    return JSONResponse(content={"message": "Se ha eliminado la película"})