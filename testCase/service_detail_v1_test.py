from common.common import data
from copy import deepcopy

from common.common import thirddata
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Detail_V1(unittest.TestCase):
    '''
    获取美购详情
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_service_detail_v1")))
    @require_login
    def test_service_detail_v1(self,value):
        mytuple = shopcart_info_get()

        inner_data = {}
        inner_data['coupon_info_id'] = thirddata['/api/service/detail/v1']['coupon_info_id']
        inner_data['is_gray'] = thirddata['/api/service/detail/v1']['is_gray']
        inner_data['referrer'] = thirddata['/api/service/detail/v1']['referrer']
        inner_data['service_id'] = mytuple[2]
        inner_data['service_item_id'] = mytuple[1]
        inner_data['transparent_key'] = mytuple[3]  # 'rm_r63bkpbh_0'
        gmhttp.params.update(inner_data)
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])
        service_id = r['data']['service_features']['pre_coupons']['coupon_url'].split('=')[2].split('&')[0]
        return service_id

    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Detail_V1.run()