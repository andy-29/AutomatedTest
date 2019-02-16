import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Auto_Complete_Bodypart(unittest.TestCase):
    '''
    美容项目搜索
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_auto_complete_bodypart")))
    def test_auto_complete_bodypart(self, value):
        self._testMethodDoc = '美容项目搜索'
        gmhttp.params.update(value.get('paramsdata'))
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        if r.get('data'):
            for item in r.get('data'):
                self.assertIn('tag_id', item.keys())
                self.assertIn('name', item.keys())
                self.assertIn(value.get('paramsdata').get('q'), item.get('name'))

    @data(*(get_values(func, "test_auto_complete_bodypart_null")))
    def test_auto_complete_bodypart_null(self, value):
        self._testMethodDoc = '美容项目搜索'
        gmhttp.params.update(value.get('paramsdata'))
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertTrue(r, value.get('assertdata'))

    def tearDown(self):
        pass


if __name__ == "__main__":
    Auto_Complete_Bodypart.run()
