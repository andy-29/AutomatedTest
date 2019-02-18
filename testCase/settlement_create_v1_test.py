import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Settlement_Create_V1(unittest.TestCase):
    '''
    创建结算单
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_settlement_create_v1")))
    @require_login
    def test_settlement_create_v1(self, value):
        self._testMethodDoc = "--"
        '''
        创建结算单
        '''
        data = {"service_item_id": "78123", "number": "1", "phone": "77777777777", "platform_coupon_id": "",
                "doctor_coupon_id": "", "use_point": "0", "is_doctor_see": "1", "insurance_info": "[]"}
        r = gmhttp.post(url=self.url, data=data).json()
        self.assertEqual(0, r['error'])
        self.st_id = r.get('data').get('id')

    def tearDown(self):
        #取消订单，防止占用sku数量
        url = self.host + g.get_info('api_info','settlement_delete')
        data = {
            "id":self.st_id,
            "cancel_reason_value":2
        }
        gmhttp.post(url=url, data=data).json()


if __name__ == "__main__":
    Settlement_Create_V1.run()
