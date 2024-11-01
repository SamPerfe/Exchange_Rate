import sys
import unittest
from os.path import dirname

library_path = dirname(dirname(__file__)) + r"/src"
sys.path.append(library_path)

import utils

class test(unittest.TestCase):

    def test_real_time_exchange_rate(self):

        """
        Test performed with result value at 1° Nov 2024
        """

        curr_base,curr_dest="eur","usd"

        result = float(1.0868)
        test = utils.get_price(from_curr=curr_base, to_curr=curr_dest)

        msg_fail = "Please check the currency symbols"

        self.assertAlmostEqual(result,test,None,msg_fail,0.001)

if __name__=="__main__":
    unittest.main()