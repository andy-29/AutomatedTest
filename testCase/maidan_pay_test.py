import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Maidan_Pay(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_maidan_pay")))
    def test_maidan_pay(self,value):
        '''
        
        '''
        myid = Maidan_Create().test_maidan_create()
        inner_data = deepcopy(data)
        inner_data['id'] = myid
        r = gmhttp.get(url=back_end_domain + myurl['/api/maidan/pay'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        pprint(dict_json)
        # print(myid)
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Pay.run()