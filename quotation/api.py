from threading import Thread

from . import eq
from . import ts


class SimpleDataCache(object):
    def __init__(self):
        self.data = None
        self.source = None

    def put(self, data, source=None):
        self.data = data
        self.source = source

    def get(self):
        while self.data is None:
            continue
        return self.data


def get_quotation(order_book_ids):
    cache = SimpleDataCache()

    Thread(target=eq.get_quotation, args=(order_book_ids, cache)).start()
    Thread(target=ts.get_quotation, args=(order_book_ids, cache)).start()

    return cache.get()
