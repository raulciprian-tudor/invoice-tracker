from fastapi import APIRouter, HTTPException, Response, status

from invoice_tracker.clients.schemas import Client

router = APIRouter()

mock_data: list[Client] = [
    Client(
        client_id="1",
        first_name="Sam",
        last_name="Winchester",
        address="On the road",
        email="sam.winchester@gmail.com",
        company="Supernatural",
    ),
    Client(
        client_id="2",
        first_name="Dean",
        last_name="Winchester",
        address="On the road",
        email="dean.winchester@gmail.com",
        company="Supernatural",
    ),
]


# Create client
@router.post("/clients/", status_code=201)
async def create_client(client: Client):
    new_id = max((int(item.client_id) for item in mock_data), default=0) + 1
    new_client = client.model_copy(update={"client_id": str(new_id)})
    mock_data.append(new_client)
    return new_client


# Get all clients
@router.get("/clients", response_model=list[Client])
async def get_clients():
    return mock_data


# Get client by ID
@router.get("/clients/{client_id}", response_model=Client)
async def get_client_by_id(client_id: str):
    for client in mock_data:
        if client.client_id == client_id:
            return client

    raise HTTPException(
        status_code=400, detail=f"Client with ID:{client_id} not found."
    )


# Update client
@router.put("/clients/{item_id}", response_model=Client)
def update_client(client_id: str, updated_client: Client):
    for index, existing_client in enumerate(mock_data):
        if existing_client.client_id == client_id:
            updated_client = updated_client.model_copy(update={"client_id": client_id})
            mock_data[index] = updated_client
            return updated_client

    raise HTTPException(status_code=404, detail="Client not found")


# Delete client
@router.delete("/clients/{item.id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: str):
    for existing_client in mock_data:
        if existing_client.client_id not in mock_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Client not found."
            )
        del existing_client

    return Response(status_code=status.HTTP_204_NO_CONTENT)
