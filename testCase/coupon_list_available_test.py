import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Coupon_List_Available(unittest.TestCase):
    '''
    可用美券列表页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_coupon_list_available")))
    def test_coupon_list_available(self,value):
        '''
        可用美券列表页
        '''
        mytuple = Settlement_Preview_V1().test_settlement_preview_v1()
        inner_data = deepcopy(data)
        # cart_item_info = [{"id": "2795972", "service_item_id": "320663", "number": "1"}]
        post_data = dict()
        post_data['cart_item_info'] = '[{"id": "' + mytuple[0] + '", "service_item_id": "'+mytuple[1] + '", "number": "1"}]'
        post_data[seconddata[0][0]] = seconddata[0][1]
        post_data['coupon_type'] = thirddata['/api/coupon/list/available']['coupon_type']
        post_data[seconddata[1][0]] = seconddata[1][1]
        post_data['valid_only'] = thirddata['/api/coupon/list/available']['valid_only']
        r = gmhttp.post(url=back_end_domain + myurl['/api/coupon/list/available'],
                          params=inner_data, cookies=cookies, data=post_data)
        dict_json = json.loads(r.content.decode())
        # pprint(dict_json)
        self.assertEqual(0, dict_json['error'])




    def tearDown(self):
        pass


if __name__ == "__main__":
    Coupon_List_Available.run()