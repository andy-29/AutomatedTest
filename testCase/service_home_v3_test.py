import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Home_V3(unittest.TestCase):
    '''
    美购首页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_service_home_v3")))
    def test_service_home_v3(self,value):
        self._testMethodDoc = "--"
        '''
        美购首页
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('specials', r.get('data').keys())
        for item in r.get('data').get('specials'):
            self.assertIn('banner_id', item.keys())
            self.assertIsInstance(item.get('banner_id'), int)
            self.assertIn('banner_url', item.keys())
            self.assertIsInstance(item.get('banner_url'), str)
            self.assertIn('banner_pic', item.keys())
            self.assertIsInstance(item.get('banner_pic'), str)
            self.assertIn('rank_mode', item.keys())
            self.assertIsInstance(item.get('rank_mode'), str)
            self.assertIn('special_id', item.keys())
            self.assertIsInstance(item.get('special_id'), int)
            self.assertIn('services', item.keys())
            self.assertIsInstance(item.get('services'), list)
        self.assertIn('seckill', r.get('data').keys())
        if 'welfare_home_float' in r.get('data').keys():
            self.assertIn('welfare_home_float_text', r.get('data').get('welfare_home_float').keys())
            self.assertIsInstance(r.get('data').get('welfare_home_float').get('welfare_home_float_text'), str)
            self.assertIn('welfare_home_float_url', r.get('data').get('welfare_home_float').keys())
            self.assertIsInstance(r.get('data').get('welfare_home_float').get('welfare_home_float_url'), str)
            self.assertIn('welfare_home_float_image', r.get('data').get('welfare_home_float').keys())
            self.assertIsInstance(r.get('data').get('welfare_home_float').get('welfare_home_float_image'), str)
        # self.assertIn('scene_bg', r.get('data').keys())
        # self.assertIn('scene', r.get('data').keys())
        if 'scene' in r.get('data').keys():
            for item in r.get('data').get('scene'):
                self.assertIn('dec_color', item.keys())
                self.assertIsInstance(item.get('dec_color'), str)
                self.assertIn('title_color', item.keys())
                self.assertIsInstance(item.get('title_color'), str)
                self.assertIn('img', item.keys())
                self.assertIsInstance(item.get('img'), str)
                self.assertIn('title', item.keys())
                self.assertIsInstance(item.get('title'), str)
                self.assertIn('url', item.keys())
                self.assertIsInstance(item.get('url'), str)
                self.assertIn('need_login', item.keys())
                self.assertIsInstance(item.get('need_login'), bool)
                self.assertIn('dec', item.keys())
                self.assertIsInstance(item.get('dec'), str)
        self.assertIn('slides', r.get('data').keys())
        for item in r.get('data').get('slides'):
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('title', item.keys())
            self.assertIsInstance(item.get('title'), str)
            self.assertIn('slide_img', item.keys())
            self.assertIsInstance(item.get('slide_img'), str)
            self.assertIn('slide_url', item.keys())
            self.assertIsInstance(item.get('slide_url'), str)
            self.assertIn('new_slide_img', item.keys())
            self.assertIsInstance(item.get('new_slide_img'), str)
            self.assertIn('slide_img_big', item.keys())
            self.assertIsInstance(item.get('slide_img_big'), str)
        self.assertIn('groups', r.get('data').keys())
        for item in r.get('data').get('groups'):
            self.assertIn('url', item.keys())
            self.assertIsInstance(item.get('url'), str)
            self.assertIn('index', item.keys())
            self.assertIsInstance(item.get('index'), int)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
            self.assertIn('icon', item.keys())
            self.assertIsInstance(item.get('icon'), str)
        self.assertIn('offset', r.get('data').keys())
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
        self.assertIn('hongbao_gift_url', r.get('data').keys())
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Home_V3.run()