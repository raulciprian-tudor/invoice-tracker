from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class ClientFields(BaseModel):
    first_name: str = Field(min_length=1, max_length=99)
    last_name: str = Field(min_length=1, max_length=99)
    address: str | None = None
    email: EmailStr
    company: str | None = None


class ClientCreate(ClientFields):
    pass


class ClientUpdate(ClientFields):
    pass


class Client(ClientFields):
    client_id: UUID
