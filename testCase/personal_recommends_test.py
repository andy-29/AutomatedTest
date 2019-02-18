import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Personal_Recommends(unittest.TestCase):
    """

    """

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        cls.diary_id = diary_id_get()

    @data(*(get_values(func, "test_personal_recommends")))
    @require_login
    def test_personal_recommends(self, value):
        self._testMethodDoc = "--"
        """

        """
        #from_type 有diary，answer，topic(专栏)，question
        gmhttp.params.update({'from_type':"diary","id":self.diary_id})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Personal_Recommends.run()
