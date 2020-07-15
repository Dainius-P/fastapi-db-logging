from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class NameItem(BaseModel):
    name: str

@router.get("/get_test/")
async def test_get(name: str):
    return {"hello": name}

@router.post("/post_test/")
async def test_post(item: NameItem):    
    return item.dict()