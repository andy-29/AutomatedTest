import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Maidan_Detail(unittest.TestCase):
    '''
    买单订单详情
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_maidan_detail")))
    def test_maidan_detail(self,value):
        '''
        买单订单详情
        '''
        myid = Maidan_Create().test_maidan_create()
        # print(myid)
        inner_data = deepcopy(data)
        inner_data['id'] = myid
        r = gmhttp.get(url=back_end_domain + myurl['/api/maidan/detail'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])
        return dict_json['data']['order_id']  # 获取订单ID

    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Detail.run()