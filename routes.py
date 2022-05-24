from fastapi import APIRouter
from blog import blog

routes = APIRouter()


routes.include_router(blog.router, prefix="/blog")


