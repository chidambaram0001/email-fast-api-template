from pydantic import BaseModel,EmailStr,Field

class SendEmailRequest(BaseModel):
    to:list[EmailStr] = Field(min_length=1)
    sub:str = Field(min_length=1, max_length=200)   
    body:str = Field(min_length=1)
    template_id:str = Field(min_length=1, max_length=200)
    html:bool = False
    tmp_tokens:dict | None = None