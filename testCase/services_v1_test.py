import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Services_V1(unittest.TestCase):
    '''
    740美购列表筛选
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_services_v1")))
    def test_services_v1(self,value):
        '''
        740美购列表筛选
        '''
        myid ,*_= shopcart_info_get()
        inner_data ={'area_id': '',
                                  'count': '10',
                                  'doctor_id': '',
                                  'hospital_id': '',
                                  'max_price': '',
                                  'min_price': '',
                                  'more_filters': '',
                                  'offset': '',
                                  'order_by': '0',
                                  'tag_id': '',
                                  'tag_ids': ''
                                  }
        r = gmhttp.get(url=self.url).json()
        self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Services_V1.run()