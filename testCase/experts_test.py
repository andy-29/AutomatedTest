import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Experts(unittest.TestCase):
    '''
    获取专家列表
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_experts")))
    @require_login
    def test_experts(self,value):
        self._testMethodDoc = "--"
        '''
        获取专家列表
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIn('experts',r.get('data').keys())
        for item in r['data']['experts']:
            self.assertIn('accept_call',item.keys())
            self.assertIn(item.get('accept_call'),[True,False])
            self.assertIn('accept_private_msg',item.keys())
            self.assertIn(item['accept_private_msg'],[True,False])
            self.assertIn('ad_str',item.keys())
            self.assertIn('badges',item.keys())
            self.assertIsInstance(item['badges'],list)
            self.assertIn('cases', item.keys())
            self.assertIsInstance(item['cases'],list)
            if item['cases']:
                for m in item['cases']:
                    self.assertIn('name',m.keys())
                    self.assertIn('tag_id',m.keys())
            self.assertIn('did', item.keys())
            self.assertIn('display_tags', item.keys())
            self.assertIsInstance(item['display_tags'], list)
            self.assertIn('distance', item.keys())
            self.assertIn('doctor_id', item.keys())
            self.assertIn('has_v_certification', item.keys())
            self.assertIn(item['has_v_certification'], [True, False])
            self.assertIn('hospital', item.keys())
            self.assertIn('hospital_id', item.keys())
            self.assertIn('hospital_type', item.keys())
            self.assertIn('is_hospital', item.keys())
            self.assertIn(item['is_hospital'], [True, False])
            self.assertIn('is_recommend', item.keys())
            self.assertIn(item['is_recommend'], [True, False])
            self.assertIn('items', item.keys())
            self.assertIsInstance(item['items'], list)
            self.assertIn('last_active_time', item.keys())
            self.assertIn('name', item.keys())
            self.assertIn('portrait', item.keys())
            self.assertIn('rate', item.keys())
            self.assertIn('service_num', item.keys())
            if item['service_num']:
                for m in item['services']:
                    self.assertIn('city',m.keys())
                    self.assertIn('default_price',m.keys())
                    self.assertIn('doctor_name',m.keys())
                    self.assertIn('gm_url',m.keys())
                    self.assertIn('image_header',m.keys())
                    self.assertIn('is_price_range',m.keys())
                    self.assertIn('name',m.keys())
                    self.assertIn('price',m.keys())
                    self.assertIn('service_id',m.keys())
                    self.assertIn('service_name',m.keys())
            self.assertIn('share_amount', item.keys())
            self.assertIn('show_rating', item.keys())
            self.assertIn('show_v', item.keys())
            self.assertIn('subscribe_num', item.keys())
            self.assertIn('title', item.keys())
            self.assertIn('voucher_num', item.keys())

        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Experts.run()