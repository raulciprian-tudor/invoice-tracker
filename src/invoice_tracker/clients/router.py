from fastapi import APIRouter

client = APIRouter(
    prefix="/clients", tags=["clients"], responses={404: {"descrition": "Not found"}}
)
