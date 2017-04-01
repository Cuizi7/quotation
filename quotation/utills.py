CODE_MAPPING = {
    "sh": "000001.XSHG",
    "sz": "399001.XSHE",
    "sz50": "000016.XSHG",
    "hs300": "000300.XSHG",
    "sz500": "000905.XSHG",
    "zxb": "399005.XSHE",
    "cyb": "399006.XSHE",
}


def code_2_order_book_id(code):
    try:
        return CODE_MAPPING[code]
    except KeyError:
        if code.startswith("6"):
            return "{}.XSHG".format(code)
        elif code[0] in ["3", "0"]:
            return "{}.XSHE".format(code)
        else:
            raise RuntimeError("Unknown code")


def order_book_id_2_code(order_book_id):
    return order_book_id.split(".")[0]
