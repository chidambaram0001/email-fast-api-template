from fastapi import FastAPI, Depends
import uvicorn
from email_service.core.config import settings


from email_service.service.send import EmailApplicationService
from email_service.model.emailmodel import SendEmailRequest
from email_service.infrastructure.smtpmailer import SmtpMailer
from email_service.infrastructure.microsoftgraph import GraphAPIMailer
from email_service.model.template_request import TemplateRequest
from email_service.infrastructure.template_repos import EmailRepository
from email_service.service.template import TemplateService
from sqlalchemy.ext.asyncio import AsyncSession
from email_service.infrastructure.database.dependencies import get_db

app = FastAPI(
    title="email svc",
)



@app.get("/")
def health_check():
    return {
        "status": "email svc UP 123",
    }



@app.post("/v1/emails")
async def Email(request:SendEmailRequest, db:AsyncSession = Depends(get_db)) :
    template_provider = EmailRepository(db)
    provider = SmtpMailer(template_provider)
    email_service = EmailApplicationService(provider)
    await email_service.send_email(request)
    return {
        "message": "Email accepted for processing"
    }

@app.post("/v2/emails")
async def GraphEmail(request:SendEmailRequest, db:AsyncSession = Depends(get_db)) :
    GraphProvider = GraphAPIMailer()
    email_service =EmailApplicationService(GraphProvider)
    await email_service.send_email(request)
    return {
        "message": "Email accepted by graph for processing"
    }

@app.post("/v1/templates")
async def RegisterTemplate(request: TemplateRequest, db:AsyncSession = Depends(get_db)):
    try:
        template_provider = EmailRepository(db)
        template_service = TemplateService(template_provider)
        id =  await template_service.save_template(request)
        return {
            "message": "template created successfully",
            "id" : id
        }
    except:
        return{
            "message": "error in template creation"
        }

@app.get("/v1/templates")
async def GetAllTempaltes(db:AsyncSession = Depends(get_db)):
    template_provider = EmailRepository(db)
    template_service = TemplateService(template_provider)
    return await template_service.get_tempaltes()

if __name__ == "__main__":
    uvicorn.run(
        "email_service.main:app",
        host="127.0.0.1",
        port=settings.port,
        reload=True
    )