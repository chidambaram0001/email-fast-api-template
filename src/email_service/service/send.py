from abc import ABC,abstractmethod
from email_service.model.emailmodel import SendEmailRequest
from email_service.model.template_request import TemplateRequest
class EmailProvider(ABC):
    @abstractmethod
    async def SendMail(self, SendEmailRequest) -> None :
        Pass  

class EmailApplicationService:

    def __init__(self, provider: EmailProvider):
        self.provider = provider

    async def send_email(self, request: SendEmailRequest) -> None:
        await self.provider.SendMail(request)
    
   
        