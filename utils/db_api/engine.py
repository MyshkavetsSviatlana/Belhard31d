from sqlalchemy import create_engine
from sqlalchemy.orm import Session


DATABASE_URL: str = 'sviatlana:sviatlana@localhost:5432/shopclass'
engine = create_engine(f'postgresql+psycopg2://{DATABASE_URL}')


def create_session(func):
    def wrapper(**kwargs):
        with Session(bind=engine) as session:
            return func(**kwargs, session=session)
    return wrapper
