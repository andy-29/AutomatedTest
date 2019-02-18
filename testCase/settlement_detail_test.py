import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Settlement_Detail(unittest.TestCase):
    '''
    取消订单
    '''

    @classmethod
    @require_login
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        print(cls.url)
        '''
        创建结算单
        '''
        data = {"service_item_id": "78123", "number": "1", "phone": "77777777777", "platform_coupon_id": "",
                "doctor_coupon_id": "", "use_point": "0", "is_doctor_see": "1", "insurance_info": "[]"}
        r = gmhttp.post(url=cls.host + g.get_info('api_info', 'settlement_create_v1'), data=data).json()
        cls.st_id = r.get('data').get('id')

    @data(*(get_values(func, "test_settlement_detail")))
    @require_login
    def test_settlement_detail(self, value):
        self._testMethodDoc = "查看订单详情"
        gmhttp.params.update({"id":self.st_id})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get('error'),0)
    def tearDown(self):
        '取消订单'
        data = {
            "id": self.st_id,
            "cancel_reason_value": 2
        }
        gmhttp.post(url=g.host + g.get_info('api_info','settlement_delete'), data=data).json()


if __name__ == "__main__":
    Settlement_Detail.run()
