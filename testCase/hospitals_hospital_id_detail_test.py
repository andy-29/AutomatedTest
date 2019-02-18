import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Hospitals_Detail(unittest.TestCase):
    '''
    查看机构详情
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        _, cls.hospital_id, *_ = service_id_get()
    @data(*(get_values(func, "test_hospitals_hospital_id_detail")))
    def test_hospitals_hospital_id_detail(self,value):
        '''
        查看机构详情
        '''
        r = gmhttp.get(self.url.format(self.hospital_id)).json()
        self.assertIs(0,r.get('error'))
        # self.assertIn('base_info', r.get('data').keys())
        # # self.assertIn('bed_count', r.get('data').get('base_info').keys())
        # # self.assertIsInstance(r.get('data').get('base_info').get('bed_count'), int)
        # self.assertIn('doctor_amount', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('doctor_amount'), int)
        # self.assertIn('device_detail', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('device_detail'), str)
        # self.assertIn('env_rating', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('env_rating'), float)
        # self.assertIn('good_at', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('good_at'), list)
        # self.assertIn('portrait', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('portrait'), str)
        # self.assertIn('hospital_name', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('hospital_name'), str)
        # self.assertIn('honor_introduction', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('honor_introduction'), str)
        # self.assertIn('hospital_classify', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('hospital_classify'), (type(None),str))
        # self.assertIn('operate_tags', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('operate_tags'), list)
        # self.assertIn('establishing_time', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('establishing_time'), (type(None),str))
        # self.assertIn('attitude_rating', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('attitude_rating'), float)
        # self.assertIn('show_v', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('show_v'), str)
        # self.assertIn('latitude', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('latitude'), float)
        # self.assertIn('effect_rating', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('effect_rating'), float)
        # self.assertIn('star', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('star'), float)
        # self.assertIn('practice_papers', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('practice_papers'), str)
        # # self.assertIn('area_count', r.get('data').get('base_info').keys())
        # # self.assertIsInstance(r.get('data').get('base_info').get('area_count'), int)
        # self.assertIn('qualification_papers', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('qualification_papers'), str)
        # self.assertIn('sell_amount', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('sell_amount'), int)
        # # self.assertIn('department_count', r.get('data').get('base_info').keys())
        # # self.assertIsInstance(r.get('data').get('base_info').get('department_count'), int)
        # self.assertIn('address', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('address'), str)
        # self.assertIn('honor_pics', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('honor_pics'), list)
        # self.assertIn('hospital_id', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('hospital_id'), str)
        # self.assertIn('device_images', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('device_images'), list)
        # self.assertIn('longitude', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('longitude'), float)
        # self.assertIn('introduction', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('introduction'), str)
        # self.assertIn('diary_amount', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('diary_amount'), int)
        # # self.assertIn('special_service', r.get('data').get('base_info').keys())
        # # self.assertIsInstance(r.get('data').get('base_info').get('special_service'), dict)
        # self.assertIn('hospital_type', r.get('data').get('base_info').keys())
        # self.assertIsInstance(r.get('data').get('base_info').get('hospital_type'), str)
        # self.assertIn('tab', r.get('data').keys())
        # self.assertIn('index', r.get('data').get('tab').keys())
        # self.assertIsInstance(r.get('data').get('tab').get('index'), bool)
        # self.assertIn('service', r.get('data').get('tab').keys())
        # self.assertIsInstance(r.get('data').get('tab').get('service'), bool)
        # self.assertIn('doctor', r.get('data').get('tab').keys())
        # self.assertIsInstance(r.get('data').get('tab').get('doctor'), bool)
        # self.assertIn('publish', r.get('data').get('tab').keys())
        # self.assertIsInstance(r.get('data').get('tab').get('publish'), bool)
        # self.assertIn('diary', r.get('data').get('tab').keys())
        # self.assertIsInstance(r.get('data').get('tab').get('diary'), bool)
        # self.assertIn('answer', r.get('data').get('tab').keys())
        # self.assertIsInstance(r.get('data').get('tab').get('answer'), bool)
        # self.assertIn('image_header_area', r.get('data').keys())
        # self.assertIn('images_counts', r.get('data').get('image_header_area').keys())
        # self.assertIsInstance(r.get('data').get('image_header_area').get('images_counts'), int)
        # self.assertIn('hospital_images', r.get('data').get('image_header_area').keys())
        # self.assertIsInstance(r.get('data').get('image_header_area').get('hospital_images'), list)
        # self.assertIn('video_pic', r.get('data').get('image_header_area').keys())
        # self.assertIsInstance(r.get('data').get('image_header_area').get('video_pic'), str)
        # self.assertIn('video_url', r.get('data').get('image_header_area').keys())
        # self.assertIsInstance(r.get('data').get('image_header_area').get('video_url'), str)
        # self.assertIn('buy_related', r.get('data').keys())
        # self.assertIn('gifts', r.get('data').get('buy_related').keys())
        # self.assertIsInstance(r.get('data').get('buy_related').get('gifts'), list)
        # self.assertIn('notice', r.get('data').get('buy_related').keys())
        # self.assertIsInstance(r.get('data').get('buy_related').get('notice'), (type(None),str))
        # self.assertIn('gift_desc', r.get('data').get('buy_related').keys())
        # self.assertIsInstance(r.get('data').get('buy_related').get('gift_desc'), str)
        # # self.assertIn('assured_to_buy', r.get('data').get('buy_related').keys())
        # # self.assertIsInstance(r.get('data').get('buy_related').get('assured_to_buy'), dict)
        # self.assertIn('related', r.get('data').keys())
        # self.assertIn('accept_call', r.get('data').get('related').keys())
        # self.assertIsInstance(r.get('data').get('related').get('accept_call'), bool)
        # self.assertIn('is_following', r.get('data').get('related').keys())
        # self.assertIsInstance(r.get('data').get('related').get('is_following'), bool)
        # self.assertIn('doctor_amount', r.get('data').get('related').keys())
        # self.assertIsInstance(r.get('data').get('related').get('doctor_amount'), int)
        # self.assertIn('phone_ext_desc', r.get('data').get('related').keys())
        # self.assertIsInstance(r.get('data').get('related').get('phone_ext_desc'), str)
        # self.assertIn('accept_private_msg', r.get('data').get('related').keys())
        # self.assertIsInstance(r.get('data').get('related').get('accept_private_msg'), bool)
        # self.assertIn('user_id', r.get('data').get('related').keys())
        # self.assertIsInstance(r.get('data').get('related').get('user_id'), int)
        # self.assertIn('call_url', r.get('data').get('related').keys())
        # self.assertIsInstance(r.get('data').get('related').get('call_url'), str)
        # self.assertIn('doctor_id', r.get('data').get('related').keys())
        # self.assertIsInstance(r.get('data').get('related').get('doctor_id'), str)
        # self.assertIn('share_data', r.get('data').keys())
        # self.assertIn('qq', r.get('data').get('share_data').keys())
        # self.assertIsInstance(r.get('data').get('share_data').get('qq'), dict)
        # self.assertIn('weibo', r.get('data').get('share_data').keys())
        # self.assertIsInstance(r.get('data').get('share_data').get('weibo'), dict)
        # self.assertIn('url', r.get('data').get('share_data').keys())
        # self.assertIsInstance(r.get('data').get('share_data').get('url'), str)
        # self.assertIn('image', r.get('data').get('share_data').keys())
        # self.assertIsInstance(r.get('data').get('share_data').get('image'), str)
        # self.assertIn('wechatmini', r.get('data').get('share_data').keys())
        # self.assertIsInstance(r.get('data').get('share_data').get('wechatmini'), dict)
        # self.assertIn('wechat', r.get('data').get('share_data').keys())
        # self.assertIsInstance(r.get('data').get('share_data').get('wechat'), dict)
        # self.assertIn('wechatline', r.get('data').get('share_data').keys())
        # self.assertIsInstance(r.get('data').get('share_data').get('wechatline'), dict)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Hospitals_Detail.run()