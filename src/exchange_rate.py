import utils

def get_real_time_exchange_rate(from_curr:str, to_curr:str) -> str:

    from_curr, to_curr = utils.get_upper(from_curr), utils.get_upper(to_curr)

    try:
        exchange_rate = utils.get_price(from_curr,to_curr)

    except RuntimeError as err:
        raise RuntimeError(
            "Please check the currency symbols. If they're right, wait for a few minute to reperforme the code"
                           ) from err 
    
    return f"{exchange_rate} {to_curr}/{from_curr}"