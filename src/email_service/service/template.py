from abc import ABC,abstractmethod
from email_service.model.template_request import TemplateRequest
from sqlalchemy.ext.asyncio import AsyncSession
from email_service.model.db.email_template import EmailTemplate
from datetime import datetime, timezone
class EmailTemplateProvider(ABC):
    @abstractmethod
    async def SaveTemplate(self, TemplateRequest) -> None :
        Pass  

class  TemplateService:

    def __init__(self, provider: EmailTemplateProvider):
        self.provider = provider

    async def save_template(self,request:TemplateRequest):
        template = EmailTemplate(
            template_key=request.template_key,
            name=request.name,
            description = request.description,
            subject_template=request.subject_template,
            body_html=request.body_html,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        return await self.provider.SaveTemplate(template)

    async def get_tempaltes(self) -> list[EmailTemplate]:
        return await self.provider.get_all_Tempaltes()