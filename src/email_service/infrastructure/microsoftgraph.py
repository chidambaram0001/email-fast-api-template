from email_service.model.emailmodel import SendEmailRequest
from email_service.service.send import EmailProvider
class GraphAPIMailer(EmailProvider):
    async def SendMail(self, request: SendEmailRequest)-> None:
        print("sending email using graph api")