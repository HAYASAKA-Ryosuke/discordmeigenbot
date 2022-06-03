import unittest
from unittest.mock import patch

from money_convert import calc_exchange

class MoneyConvertTest(unittest.TestCase):
    def test_指定した金額が想定どおりのフォーマットで返ってくるか(self):
        with patch('money_convert._fetch_exchange') as mock_fetch_exchange:
            mock_fetch_exchange.return_value = 130.12345
            self.assertEqual(calc_exchange(100000, 'USD', 'JPY'), 'USD: 100,000 → JPY: 13,012,345')
            mock_fetch_exchange.return_value = 0.00764356
            self.assertEqual(calc_exchange(100000000, 'JPY', 'USD'), 'JPY: 100,000,000 → USD: 764,356')
