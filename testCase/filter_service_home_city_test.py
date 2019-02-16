import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Filter_Service_Home_City(unittest.TestCase):
    '''
    首页选择城市
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_filter_service_home_city")))
    def test_filter_service_home_city(self,value):
        '''
        首页选择城市
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIn('auto_located',r.get("data"))
        self.assertIn('countries',r.get("data"))
        city_num = 0
        for item in r.get("data").get("countries"):
            self.assertIn("is_located",item.keys())
            self.assertIn("name",item.keys())
            self.assertIn("groups",item.keys())
            for sub_item in item.get("groups"):
                self.assertIn("is_hot", sub_item.keys())
                self.assertIn("initial", sub_item.keys())
                self.assertIn("cities", sub_item.keys())
                self.assertIn("title", sub_item.keys())
                for sub2_item in sub_item.get("cities"):
                    if sub_item.get('is_hot') != True:
                        self.assertIn("tag_id",sub2_item.keys())
                    self.assertIn("id", sub2_item.keys())
                    self.assertIn("name", sub2_item.keys())
                    city_num +=1
        print('用例执行完毕,一共有{}个城市！'.format(city_num))


    def tearDown(self):
        pass


if __name__ == "__main__":
    Filter_Service_Home_City.run()