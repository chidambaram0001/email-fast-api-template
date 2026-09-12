from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from email_service.infrastructure.database.db import async_session_local

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_local() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise