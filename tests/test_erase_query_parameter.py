import unittest

from erase_query_parameter import erase_query_parameter

class EraseQueryParameterTest(unittest.TestCase):
    def test_クエリパラメータつきのURLをなげるとクエリパラメータを除去した文字列で返ってくるか(self):
        embed = erase_query_parameter('https://example.com/foo/hoge/?ham=egg')
        self.assertEqual(embed.fields[0].name, '↑erase query param URL')
        self.assertEqual(embed.fields[0].value, '[link](https://example.com/foo/hoge/)')
