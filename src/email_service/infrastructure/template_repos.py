from sqlalchemy.ext.asyncio import AsyncSession
from email_service.service.template import EmailTemplateProvider
from email_service.model.template_request import TemplateRequest
from email_service.model.db.email_template import EmailTemplate
from sqlalchemy import select
class EmailRepository(EmailTemplateProvider):
    def __init__(self, session: AsyncSession) :
        self.session = session
    async def SaveTemplate(self, template: EmailTemplate) -> str:
        self.session.add(template)
        await self.session.commit()
        return template.id
    
    async def get_all_Tempaltes(self) -> list[EmailTemplate]:
        result = await self.session.execute(select(EmailTemplate).order_by(EmailTemplate.created_at.desc()))
        return list(result.scalars().all())
    async def get_template_by_id(self, template_id: int) -> EmailTemplate:
        result = await self.session.execute(select(EmailTemplate).where(EmailTemplate.id == template_id))
        return result.scalars().first()