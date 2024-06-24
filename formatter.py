from models import OrderInfo


def format_order_info(order_info: OrderInfo):
    result = f'Поступил новый заказ: {order_info.order_id}\n'
    result += f'Сумма: {order_info.sum} руб.\n'
    result += 'Товары:\n\n'
    for item in order_info.items:
        name, sku, price, count = item.name.split("Ноутбук")[1], item.sku, item.price, item.count
        item_link = f'https://partner.market.yandex.ru/supplier/50928838/assortment/offer-card?offerId={sku}'

        result += f'SKU: {sku}\n'
        result += f'Наименование: {name}\n'
        result += f'Ссылка: {item_link}\n'
        result += f'Стоимость: {price} руб.\n'
        result += f'Количество: {count} шт.'
        result += '\n' * 2

    return result

