from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Dict, List

app = FastAPI(title="Simple Items API")

# In-memory хранилище
items_db: Dict[int, dict] = {}
current_id = 1


class ItemIn(BaseModel):
    name: str
    price: float

    @field_validator('price', mode='before')
    def validate_price(v: float):
        if v < 0.001:
            raise ValueError('Price must be greater of 0.001')
        
        return v


class ItemOut(ItemIn):
    id: int


@app.get("/items", response_model=List[ItemOut])
async def list_items():
    """Получить список всех товаров."""
    return [{"id": item_id, **item} for item_id, item in items_db.items()]


@app.get("/items/{item_id}", response_model=ItemOut)
async def get_item(item_id: int):
    """Получить товар по ID."""
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **item}


@app.post("/items", response_model=ItemOut, status_code=200)
async def create_item(item: ItemIn):
    """Создать новый товар."""
    global current_id
    item_id = current_id
    items_db[item_id] = item.__dict__
    current_id += 1
    return {"id": item_id, **item.__dict__}


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """Удалить товар по ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return