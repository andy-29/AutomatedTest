import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Coupon_Recommend(unittest.TestCase):
    '''
    美券列表页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_recommend_list")))
    def test_recommend_list(self,value):
        self._testMethodDoc = "--"
        '''
        美券推荐
        '''
        serviec_id ,*_= service_id_get()
        self._testMethodDoc = '美券推荐'
        gmhttp.params.update({
            "service_id":serviec_id,
            "service_item_id":'',
            "groupbuy_price_id":''
        })
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Coupon_Recommend.run()