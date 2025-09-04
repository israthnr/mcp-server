from fastapi import APIRouter
from app.models.cv_models import CVQuery
import json

router = APIRouter()

# Load resume data
with open("resume.json", "r") as f:
    resume = json.load(f)

@router.post("/cv/query")
def query_cv(query: CVQuery):
    q = query.question.lower()

    if "last position" in q:
        return {"answer": resume.get("last_position", "Not found")}
    elif "skills" in q:
        return {"answer": resume.get("skills", [])}
    elif "education" in q:
        return {"answer": resume.get("education", [])}
    else:
        return {"answer": "Sorry, I don't understand the question."}
