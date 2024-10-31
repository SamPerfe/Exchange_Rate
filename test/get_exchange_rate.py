import sys
from os.path import dirname

library_path = dirname(dirname(__file__)) + r"/src"
sys.path.append(library_path)

from exchange_rate import get_real_time_exchange_rate

if __name__=="__main__":
    curr_base,curr_dest="eur","usd"
    print(get_real_time_exchange_rate(from_curr=curr_base, to_curr=curr_dest))