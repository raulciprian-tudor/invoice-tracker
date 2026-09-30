from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, Response, status

from invoice_tracker.clients.schemas import Client, ClientCreate, ClientUpdate

router = APIRouter()

mock_data: list[Client] = [
    Client(
        client_id=uuid4(),
        first_name="Sam",
        last_name="Winchester",
        address="On the road",
        email="sam.winchester@gmail.com",
        company="Supernatural",
    ),
    Client(
        client_id=uuid4(),
        first_name="Dean",
        last_name="Winchester",
        address="On the road",
        email="dean.winchester@gmail.com",
        company="Supernatural",
    ),
]


@router.post("/clients", status_code=status.HTTP_201_CREATED, response_model=Client)
async def create_client(client: ClientCreate):
    new_client = Client(client_id=uuid4(), **client.model_dump())
    mock_data.append(new_client)
    return new_client


@router.get("/clients", response_model=list[Client])
async def get_clients():
    return mock_data


@router.get("/clients/{client_id}", response_model=Client)
async def get_client_by_id(client_id: UUID):
    for client in mock_data:
        if client.client_id == client_id:
            return client

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Client with ID:{client_id} not found.",
    )


@router.put("/clients/{client_id}", response_model=Client)
async def update_client(client_id: UUID, updated_client: ClientUpdate):
    for index, existing_client in enumerate(mock_data):
        if existing_client.client_id == client_id:
            client_to_store = Client(client_id=client_id, **updated_client.model_dump())
            mock_data[index] = client_to_store
            return client_to_store

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
    )


@router.delete("/clients/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(client_id: UUID):
    for index, existing_client in enumerate(mock_data):
        if existing_client.client_id == client_id:
            del mock_data[index]
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Client not found."
    )
