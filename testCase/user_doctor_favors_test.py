import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_Doctor_Favors(unittest.TestCase):
    '''
    用户医生列表
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_user_doctor_favors")))
    def test_user_doctor_favors(self,value):
        '''
        用户医生列表
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('experts', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('experts'), list)
        for item in r.get('data').get('experts'):
            self.assertIn('dist', item.keys())
            self.assertIsInstance(item.get('dist'), int)
            self.assertIn('is_favored', item.keys())
            self.assertIsInstance(item.get('is_favored'), bool)
            self.assertIn('is_recommend', item.keys())
            self.assertIsInstance(item.get('is_recommend'), bool)
            self.assertIn('good_at', item.keys())
            self.assertIsInstance(item.get('good_at'), str)
            self.assertIn('rate', item.keys())
            self.assertIsInstance(item.get('rate'), float)
            self.assertIn('service_num', item.keys())
            self.assertIsInstance(item.get('service_num'), int)
            self.assertIn('portrait', item.keys())
            self.assertIsInstance(item.get('portrait'), str)
            self.assertIn('is_hospital', item.keys())
            self.assertIsInstance(item.get('is_hospital'), bool)
            self.assertIn('lng', item.keys())
            self.assertIsInstance(item.get('lng'), (float,int))
            self.assertIn('badges', item.keys())
            self.assertIsInstance(item.get('badges'), list)
            self.assertIn('accept_private_msg', item.keys())
            self.assertIsInstance(item.get('accept_private_msg'), bool)
            self.assertIn('title', item.keys())
            self.assertIsInstance(item.get('title'), str)
            self.assertIn('introduction', item.keys())
            self.assertIsInstance(item.get('introduction'), str)
            self.assertIn('phone_ext', item.keys())
            self.assertIsInstance(item.get('phone_ext'), str)
            self.assertIn('hospital', item.keys())
            self.assertIsInstance(item.get('hospital'), str)
            self.assertIn('exterior_service_ids', item.keys())
            self.assertIsInstance(item.get('exterior_service_ids'), list)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), str)
            self.assertIn('hospital_name', item.keys())
            self.assertIsInstance(item.get('hospital_name'), str)
            self.assertIn('city_id', item.keys())
            self.assertIsInstance(item.get('city_id'), str)
            self.assertIn('show_v', item.keys())
            self.assertIsInstance(item.get('show_v'), str)
            self.assertIn('department', item.keys())
            self.assertIsInstance(item.get('department'), str)
            self.assertIn('subscribe_num', item.keys())
            self.assertIsInstance(item.get('subscribe_num'), (str,int))
            self.assertIn('doctor_type', item.keys())
            self.assertIsInstance(item.get('doctor_type'), str)
            self.assertIn('show_rating', item.keys())
            self.assertIsInstance(item.get('show_rating'), str)
            self.assertIn('accept_call', item.keys())
            self.assertIsInstance(item.get('accept_call'), bool)
            self.assertIn('share_amount', item.keys())
            self.assertIsInstance(item.get('share_amount'), int)
            self.assertIn('hospital_scale', item.keys())
            self.assertIsInstance(item.get('hospital_scale'), str)
            self.assertIn('phone', item.keys())
            self.assertIsInstance(item.get('phone'), str)
            self.assertIn('phone_hint', item.keys())
            self.assertIsInstance(item.get('phone_hint'), str)
            self.assertIn('is_online', item.keys())
            self.assertIsInstance(item.get('is_online'), bool)
            self.assertIn('lat', item.keys())
            self.assertIsInstance(item.get('lat'), (float,int))
            self.assertIn('cases', item.keys())
            self.assertIsInstance(item.get('cases'), list)
            self.assertIn('province_id', item.keys())
            self.assertIsInstance(item.get('province_id'), str)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
            self.assertIn('did', item.keys())
            self.assertIsInstance(item.get('did'), str)
            self.assertIn('hospital_id', item.keys())
            self.assertIsInstance(item.get('hospital_id'), str)
            self.assertIn('ad_str', item.keys())
            self.assertIsInstance(item.get('ad_str'), str)
            self.assertIn('display_tags', item.keys())
            self.assertIsInstance(item.get('display_tags'), list)
            self.assertIn('operate_tags', item.keys())
            self.assertIsInstance(item.get('operate_tags'), list)
            self.assertIn('items', item.keys())
            self.assertIsInstance(item.get('items'), list)
            self.assertIn('doctor_id', item.keys())
            self.assertIsInstance(item.get('doctor_id'), str)
            self.assertIn('last_active_time', item.keys())
            self.assertIsInstance(item.get('last_active_time'), str)
            self.assertIn('hospital_type', item.keys())
            self.assertIsInstance(item.get('hospital_type'), str)
            self.assertIn('extend_tips', item.keys())
            self.assertIsInstance(item.get('extend_tips'), str)
            self.assertIn('address', item.keys())
            self.assertIsInstance(item.get('address'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    User_Doctor_Favors.run()