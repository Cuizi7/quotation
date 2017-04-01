import hug
from . import api


@hug.local()
def get_quotation(order_book_ids: hug.types.multiple):
    return api.get_quotation(order_book_ids)
