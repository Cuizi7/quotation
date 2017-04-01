import easyquotation
from six import iteritems
from dateutil.parser import parse
import numpy as np

from .utills import order_book_id_2_code, code_2_order_book_id


def get_quotation(order_book_ids, data_cache, resource='sina'):
    tick_dict = {}

    quotation = easyquotation.use(resource)

    code_list = [order_book_id_2_code(order_book_id) for order_book_id in order_book_ids]

    eq_dict = quotation.stocks(code_list)

    for code, data in iteritems(eq_dict):
        tick = {
            'order_book_id': code_2_order_book_id(code),
            'datetime': parse('%s %s' % (data['date'], data['time'])),
            'open': data['open'],
            'last': data['now'],
            'low': data['low'],
            'high': data['high'],
            'prev_close': data['close'],
            'volume': data['volume'],
            'total_turnover': data['turnover'],
            'open_interest': np.nan,
            'prev_settlement': np.nan,

            'bid': [
                data['bid1'],
                data['bid2'],
                data['bid3'],
                data['bid4'],
                data['bid5'],
            ],
            'bid_volume': [
                data['bid1_volume'],
                data['bid2_volume'],
                data['bid3_volume'],
                data['bid4_volume'],
                data['bid5_volume'],
            ],
            'ask': [
                data['ask1'],
                data['ask2'],
                data['ask3'],
                data['ask4'],
                data['ask5'],
            ],
            'ask_volume': [
                data['ask1_volume'],
                data['ask2_volume'],
                data['ask3_volume'],
                data['ask4_volume'],
                data['ask5_volume'],
            ],

            'limit_up': np.nan,
            'limit_down': np.nan,
        }
        tick_dict[code_2_order_book_id(code)] = tick
    data_cache.put(tick_dict, 'easy_quotation')
