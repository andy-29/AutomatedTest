import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Home_V3_List(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_service_home_v3_list")))
    def test_service_home_v3_list(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('services', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('services'), list)
        for item in r.get('data').get('services'):
            self.assertIn('default_price', item.keys())
            self.assertIsInstance(item.get('default_price'), int)
            self.assertIn('gengmei_price', item.keys())
            self.assertIsInstance(item.get('gengmei_price'), int)
            self.assertIn('service_name', item.keys())
            self.assertIsInstance(item.get('service_name'), str)
            self.assertIn('gm_url', item.keys())
            self.assertIsInstance(item.get('gm_url'), str)
            self.assertIn('doctor_name', item.keys())
            self.assertIsInstance(item.get('doctor_name'), str)
            self.assertIn('is_price_range', item.keys())
            self.assertIsInstance(item.get('is_price_range'), bool)
            self.assertIn('seckill_status', item.keys())
            self.assertIsInstance(item.get('seckill_status'), (str,int))
            self.assertIn('hospital_name', item.keys())
            self.assertIsInstance(item.get('hospital_name'), str)
            self.assertIn('fenqi_new_desc', item.keys())
            self.assertIsInstance(item.get('fenqi_new_desc'), str)
            self.assertIn('city', item.keys())
            self.assertIsInstance(item.get('city'), str)
            self.assertIn('ordering', item.keys())
            self.assertIsInstance(item.get('ordering'), (str,int))
            self.assertIn('has_video', item.keys())
            self.assertIsInstance(item.get('has_video'), bool)
            self.assertIn('mark_info', item.keys())
            self.assertIsInstance(item.get('mark_info'), dict)
            self.assertIn('is_seckill', item.keys())
            self.assertIsInstance(item.get('is_seckill'), bool)
            self.assertIn('sell_or_diary_num_desc', item.keys())
            self.assertIsInstance(item.get('sell_or_diary_num_desc'), str)
            self.assertIn('image_header', item.keys())
            self.assertIsInstance(item.get('image_header'), str)
            self.assertIn('seckill_price', item.keys())
            self.assertIsInstance(item.get('seckill_price'), (str,int))
            self.assertIn('hospital_scale', item.keys())
            self.assertIsInstance(item.get('hospital_scale'), str)
            self.assertIn('short_description', item.keys())
            self.assertIsInstance(item.get('short_description'), str)
            self.assertIn('operate_tag', item.keys())
            self.assertIsInstance(item.get('operate_tag'), list)
            self.assertIn('is_support_insurance', item.keys())
            self.assertIsInstance(item.get('is_support_insurance'), bool)
            self.assertIn('is_groupbuy', item.keys())
            self.assertIsInstance(item.get('is_groupbuy'), bool)
            self.assertIn('business_type', item.keys())
            self.assertIsInstance(item.get('business_type'), str)
            self.assertIn('distance', item.keys())
            self.assertIsInstance(item.get('distance'), str)
            self.assertIn('coupon_new_desc', item.keys())
            self.assertIsInstance(item.get('coupon_new_desc'), str)
            self.assertIn('payment_type', item.keys())
            self.assertIsInstance(item.get('payment_type'), str)
            self.assertIn('groupbuy_price', item.keys())
            self.assertIsInstance(item.get('groupbuy_price'), int)
            self.assertIn('service_id', item.keys())
            self.assertIsInstance(item.get('service_id'), int)
        self.assertIn('offset', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('offset'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Home_V3_List.run()