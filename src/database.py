from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://postgres:postgres@localhost/postgres'


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base = declarative_base()




async_session = sessionmaker(
    engine, class_=AsyncSession
)



async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session




