# flake8: noqa
from .dist import *
from .local import *


SQLALCHEMY_DATABASE_URI = (
    f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
