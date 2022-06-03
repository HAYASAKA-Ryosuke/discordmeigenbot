import unittest

from help import get_help_message


class HelpTest(unittest.TestCase):
    def test_ヘルプメッセージの出力メッセージを確認(self):
        self.assertEqual(get_help_message(), "!meigen: 名言表示\n!weather: 天気表示\n!EUR <price>: ユーロを円に変換\n!USD <price>: ドルを円に変換\n!URL <url>: クエリパラメータを除去")
