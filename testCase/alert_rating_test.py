import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *

@ddt
class Alert_Rating(unittest.TestCase):
    '''
    
    '''
    @classmethod
    def setUpClass(cls):
        print('获取环境信息和接口信息')
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func,"test_alert_rating")))
    @require_login
    def test_alert_rating(self,value):
        self._testMethodDoc = '标记用户评分'
        r = gmhttp.post(self.url,data=value.get('requestdata')).json()
        self.assertEqual(r,value.get('assertdata'))

    def tearDown(self):
        pass


if __name__ == "__main__":
    Alert_Rating.run()