import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Cache_Data_Data_Name(unittest.TestCase):
    '''
    筛选
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
    @data(*(get_values(func, "test_cache_data_data_name")))
    def test_cache_data_data_name(self,value):
        self._testMethodDoc = '搜索筛选器'
        r = gmhttp.get(self.url.format('experts_filter')).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('advanced_filter', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('advanced_filter'), list)
        for item in r.get('data').get('advanced_filter'):
            self.assertIn('values', item.keys())
            self.assertIsInstance(item.get('values'), list)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), str)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
        self.assertIn('areas', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('areas'), list)
        for item in r.get('data').get('areas'):
            self.assertIn('is_located', item.keys())
            self.assertIsInstance(item.get('is_located'), bool)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
            self.assertIn('groups', item.keys())
            self.assertIsInstance(item.get('groups'), list)
        self.assertIn('service_channels', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('service_channels'), list)
        for item in r.get('data').get('service_channels'):
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
        self.assertIn('orders', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('orders'), list)
        for item in r.get('data').get('orders'):
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
        self.assertIn('tags', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('tags'), list)
        for item in r.get('data').get('tags'):
            # self.assertIn('id', item.keys())
            # self.assertIsInstance(item.get('id'), str)
            self.assertIn('sub_tags', item.keys())
            self.assertIsInstance(item.get('sub_tags'), list)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Cache_Data_Data_Name.run()