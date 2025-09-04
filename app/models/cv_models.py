from pydantic import BaseModel

class CVQuery(BaseModel):
    question: str
