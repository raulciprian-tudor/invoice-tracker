from pydantic import BaseModel, EmailStr


class Client(BaseModel):
    client_id: str
    first_name: str
    last_name: str
    address: str | None = None  # optional
    email: EmailStr | None = None  # optional
    company: str | None = None  # optional
