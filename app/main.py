from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(
    title="Lab 1 REST API",
    description="CRUD REST API for laboratory work #1",
    version="1.0.0"
)


class ItemCreate(BaseModel):
    name: str
    description: str


class Item(ItemCreate):
    id: int


items = [
    Item(
        id=1,
        name="First item",
        description="First test item"
    ),
    Item(
        id=2,
        name="Second item",
        description="Second test item"
    )
]


@app.get("/api/items", response_model=list[Item])
def get_items():
    return items


@app.get("/api/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )


@app.post(
    "/api/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED
)
def create_item(item_data: ItemCreate):
    new_id = max([item.id for item in items], default=0) + 1

    new_item = Item(
        id=new_id,
        name=item_data.name,
        description=item_data.description
    )

    items.append(new_item)

    return new_item


@app.put("/api/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: ItemCreate):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated_item = Item(
                id=item_id,
                name=item_data.name,
                description=item_data.description
            )

            items[index] = updated_item

            return updated_item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )


@app.delete(
    "/api/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )