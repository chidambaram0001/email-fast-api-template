from email_service.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker

engine = create_async_engine(settings.db_connection_str, echo=True, pool_pre_ping=True)
async_session_local = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
