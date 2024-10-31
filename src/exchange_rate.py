import utils

def get_real_time_exchange_rate(from_curr:str, to_curr:str) -> str:

    from_curr, to_curr = utils.get_upper(from_curr), utils.get_upper(to_curr)
    exchange_rate = utils.get_price(from_curr,to_curr)
    
    return f"{exchange_rate} {to_curr}/{from_curr}"