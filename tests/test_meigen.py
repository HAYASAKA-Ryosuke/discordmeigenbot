import unittest
from unittest.mock import patch

from meigen import fetch_meigen


class MeigenTest(unittest.TestCase):
    def test_名言が想定どおりのフォーマットで返ってくるか確認(self):
        with patch('meigen.download_meigen') as mock_download_meigen:
            mock_download_meigen.return_value = [{"meigen":"もしも人間の価値がその仕事で決まるならば、馬はどんな人間よりも価値があるはずだ。馬はよく働くし、第一、文句を言わない。","auther":"M・ゴーリキー"}]
            self.assertEqual(fetch_meigen(), "もしも人間の価値がその仕事で決まるならば、馬はどんな人間よりも価値があるはずだ。馬はよく働くし、第一、文句を言わない。 by M・ゴーリキー")
