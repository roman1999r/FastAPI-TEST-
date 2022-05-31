from sqlalchemy.orm import Session
from .models import Post
from .schemas import PostCreate
import logging

#logging.basicConfig(level=logging.INFO, filename='sample.log', encoding='utf-8')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('sample.info')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_post_list(db: Session):
    logger.info('GET OK')
    return db.query(Post).all()


def create_post(db: Session, item: PostCreate):
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    logger.info(f'{post.title} was create {post.date}')
    print(logger)
    return post
