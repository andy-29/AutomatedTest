import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Attrinfo_Service_Id(unittest.TestCase):
    '''
    美购多属性信息
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.service_id,_,_ = service_id_get()

    @data(*(get_values(func, "test_service_attrinfo_service_id")))
    def test_service_attrinfo_service_id(self,value):
        '''
        美购多属性信息
        '''
        r = gmhttp.get(self.url.format(self.service_id)).json()
        if r.get('error') == 0:
        # self.assertEqual(r.get("error"), 0,msg=str(r) + str(url))
            self.assertIn('data', r.keys())
            self.assertIn('total_price', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('total_price'), str)
            self.assertIn('service_name', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('service_name'), str)
            self.assertIn('price', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('price'), dict)
            self.assertIn('original_price', r.get('data').get('price').keys())
            self.assertIsInstance(r.get('data').get('price').get('original_price'), str)
            self.assertIn('total_price', r.get('data').get('price').keys())
            self.assertIsInstance(r.get('data').get('price').get('total_price'), str)
            self.assertIn('gengmei_price', r.get('data').get('price').keys())
            self.assertIsInstance(r.get('data').get('price').get('gengmei_price'), str)
            self.assertIn('exchange_points_ceiling', r.get('data').get('price').keys())
            self.assertIsInstance(r.get('data').get('price').get('exchange_points_ceiling'), int)
            self.assertIn('pre_payment_price', r.get('data').get('price').keys())
            self.assertIsInstance(r.get('data').get('price').get('pre_payment_price'), str)
            self.assertIn('multiattribute', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('multiattribute'), list)
            for item in r.get('data').get('multiattribute'):
                self.assertIn('options', item.keys())
                self.assertIsInstance(item.get('options'), list)
                self.assertIn('id', item.keys())
                self.assertIsInstance(item.get('id'), int)
                self.assertIn('name', item.keys())
                self.assertIsInstance(item.get('name'), str)
            self.assertIn('points', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('points'), int)
            self.assertIn('is_seckill', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('is_seckill'), bool)
            self.assertIn('service_id', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('service_id'), int)
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Attrinfo_Service_Id.run()
