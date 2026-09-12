from pydantic import BaseModel

class TemplateRequest(BaseModel) : 
    template_key:str
    name: str
    description: str
    subject_template: str
    body_html: str

    
