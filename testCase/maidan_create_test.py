import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Maidan_Create(unittest.TestCase):
    '''
    买单提交
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_maidan_create")))
    def test_maidan_create(self,value):
        '''
        买单提交
        '''
    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        inner_data = deepcopy(data)
        post_data = {'doctor_id': doctor_id, 'payment': thirddata['/api/maidan/create']['payment'],
                     'tag_ids': thirddata['/api/maidan/create']['tag_ids']}
        r = gmhttp.post(url=back_end_domain + myurl['/api/maidan/create'],
                          params=inner_data, cookies=cookies, data=post_data)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])
        return dict_json['data']['id']

    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Create.run()
