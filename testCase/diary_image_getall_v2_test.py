import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Diary_Image_Getall_V2(unittest.TestCase):
    """

    """

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.diary_id = diary_id_get()

    @data(*(get_values(func, "test_diary_image_getall_v2")))
    def test_diary_image_getall_v2(self, value):
        self._testMethodDoc = "--"
        """

        """
        gmhttp.params.update({"diary_id":self.diary_id,"type":1})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Image_Getall_V2.run()
