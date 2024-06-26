from typing import Any
from fastapi import FastAPI, HTTPException, Request

import config
from formatter import format_order_info
from models import OrderInfo, OrderItem
from telegram import send_telegram_message


app = FastAPI()


@app.post("/order/accept")
async def accept_order(request: Request, body: dict):
    auth_token = request.headers.get("authorization")

    if auth_token != config.MARKET_AUTHORIZATION_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # parsing info from body
    order: dict[str, Any] = body.get("order", dict())
    items_data: list[dict] = order.get("items", list())
    order_id: int = order.get("id", 0)
    order_sum: int = order.get("buyerItemsTotal", 0)

    if not items_data or not order_id or not order_sum:
        raise HTTPException(status_code=400, detail="Bad request")

    items: list[OrderItem] = []
    for item in items_data:
        items.append(
            OrderItem(
                sku=item.get("shopSku", ""),
                name=item.get("offerName", ""),
                count=item.get("count", 0),
                price=item.get("buyerPrice", 0),
            )
        )

    order_info = OrderInfo(
        order_id=order_id,
        items=items,
        sum=order_sum,
    )

    send_telegram_message(format_order_info(order_info))

    return order_info


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=443, reload=True)
