import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Hospitals_Services(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        _, cls.hospital_id, *_ = service_id_get()
    @data(*(get_values(func, "test_hospitals_hospital_id_services")))
    def test_hospitals_hospital_id_services(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''

        r = gmhttp.get(self.url.format(self.hospital_id)).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('services', r.get('data').keys())
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
            self.assertIsInstance(item.get('seckill_status'), str)
            self.assertIn('hospital_name', item.keys())
            self.assertIsInstance(item.get('hospital_name'), str)
            self.assertIn('fenqi_new_desc', item.keys())
            self.assertIsInstance(item.get('fenqi_new_desc'), str)
            self.assertIn('doctor_title', item.keys())
            self.assertIsInstance(item.get('doctor_title'), str)
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
            self.assertIsInstance(item.get('seckill_price'), str)
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
        self.assertIn('total_count', r.get('data').keys())
        self.assertIn('tag_distribution', r.get('data').keys())
        if r.get('data').get('tag_distribution'):
            print(r)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Hospitals_Services.run()