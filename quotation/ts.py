import numpy as np
import tushare as ts
from dateutil.parser import parse

from .utills import code_2_order_book_id, order_book_id_2_code


def get_quotation(order_book_ids, data_cache):

    tick_dict = {}

    code_list = [order_book_id_2_code(order_book_id) for order_book_id in order_book_ids]

    df = ts.get_realtime_quotes(code_list)

    for item in df.itertuples():
        tick = {
            'order_book_id': code_2_order_book_id(item.code),
            'datetime': parse('%s %s' % (item.date, item.time)),
            'open': item.open,
            'last': item.price,
            'low': item.low,
            'high': item.high,
            'prev_close': item.pre_close,
            'volume': item.volume,
            'total_turnover': np.nan,
            'open_interest': np.nan,
            'prev_settlement': np.nan,

            'bid': [
                item.b1_p,
                item.b2_p,
                item.b3_p,
                item.b4_p,
                item.b5_p,
            ],
            'bid_volume': [
                item.b1_v,
                item.b2_v,
                item.b3_v,
                item.b4_v,
                item.b5_v,
            ],
            'ask': [
                item.a1_p,
                item.a2_p,
                item.a3_p,
                item.a4_p,
                item.a5_p,
            ],
            'ask_volume': [
                item.a1_v,
                item.a2_v,
                item.a3_v,
                item.a4_v,
                item.a5_v,
            ],

            'limit_up': np.nan,
            'limit_down': np.nan,
        }
        tick_dict[tick['order_book_id']] = tick
    data_cache.put(tick_dict, 'tushare')
