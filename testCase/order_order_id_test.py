import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Order_Order_Id(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        print('获取环境信息和接口信息')
        self.host = g.host
        self.api_name = g.api_name(os.path.basename(__file__).split('_test.py')[0])
        self.android_params = g.android_params

    @data(*(get_values(func, "test_order_order_id")))
    def test_order_order_id(self,value):
        '''
        
        '''
        inner_data_pre = deepcopy(data)
        inner_data_pre['start_num'] = '0'
        inner_data_pre['status'] = '1'
        r = gmhttp.get(url=back_end_domain + myurl['/api/orders/my/v2'],
                         params=inner_data_pre, cookies=cookies)
        dict_json_pre = json.loads(r.content.decode())
        order_id = dict_json_pre['data']['orders'][0]['order']['order_id']
        inner_data = deepcopy(data)
        r = gmhttp.get(url=back_end_domain + myurl['/api/order/{}'].format(order_id),
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        # pprint(dict_json)
        self.assertEqual(0, dict_json['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Order_Order_Id.run()