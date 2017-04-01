class DataEngine(object):
    def __init__(self):
        self._activate = False
        self._subscribed_stock = []
        self._data_cache = {}
        self._check_interval = 0.2

    def process(self, data_func):
        while self._activate:
            data_dict = data_func(self._subscribed_stock)

