from pydantic import BaseModel


class OrderItem(BaseModel):
    sku: str
    name: str
    count: int
    price: int


class OrderInfo(BaseModel):
    order_id: int
    items: list[OrderItem]
    sum: int

