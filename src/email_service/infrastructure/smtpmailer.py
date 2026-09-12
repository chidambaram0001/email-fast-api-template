from email_service.model.emailmodel import SendEmailRequest
from email_service.service.send import EmailProvider
import os
import smtplib
from email.message import EmailMessage
from email_service.core.config import settings
from email_service.infrastructure.render import Renderer
class SmtpMailer(EmailProvider):
    def __init__(self, template_provider=None):
        self.template_provider = template_provider
        self.renderer = Renderer()
    async def SendMail(self, request: SendEmailRequest)-> None:
        message = EmailMessage()
        message["From"] = settings.email_id
        message["To"] = request.to
        message["Subject"] = request.sub
        message.set_content(request.body)
        html_content = await self.template_provider.get_template_by_id(request.template_id)
        if request.html == True and html_content:
            rendered_content = html_content.body_html
            if request.tmp_tokens:
                rendered_content = self.renderer.render(rendered_content,request.tmp_tokens)
            message.add_alternative(rendered_content, subtype="html")

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(settings.email_id, settings.password)
            smtp.send_message(message)
        print("sending email using smtp")