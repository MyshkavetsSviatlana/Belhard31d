from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


DATABASE_URL: str = 'sviatlana:sviatlana@localhost:5432/shopclass'
engine = create_async_engine(f'postgresql+psycopg2://{DATABASE_URL}')


async def create_session(func):
    async def wrapper(**kwargs):
        with AsyncSession(bind=engine) as session:
            return func(**kwargs, session=session)
    return wrapper
