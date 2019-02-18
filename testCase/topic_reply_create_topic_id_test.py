import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Topic_Reply_Create_Topic_Id(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_topic_reply_create_topic_id")))
    @require_login
    def test_topic_reply_create_topic_id(self, value):
        self._testMethodDoc = "--"
        '''
        
        '''
        inner_data_pre = {}
        inner_data_pre['count'] = '10'
        inner_data_pre['face_simulator_time'] = ''
        inner_data_pre['offset'] = ''
        inner_data_pre['tabtype'] = 'choice'
        gmhttp.params.update(inner_data_pre)
        r = gmhttp.get(url=g.host + '/api/index/v6').json()
        gmhttp.reset()
        latest_topic_id = r['data']['features'][1]['diary']['latest_topic_id']
        post_data = {'content': '真好看漂亮' + str(random.randint(0, 1000000))}
        r = gmhttp.post(url=self.url.format(latest_topic_id), data=post_data).json()
        # pprint(r.content.decode().encode().decode('unicode_escape'))
        # dict_json = json.loads(r.content.decode().encode().decode('unicode_escape'))

        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Topic_Reply_Create_Topic_Id.run()
