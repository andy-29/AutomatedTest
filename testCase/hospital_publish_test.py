import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Hospital_Publish(unittest.TestCase):
    '''
    获取机构的发布内容
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        _, cls.hospital_id, *_ = service_id_get()

    @data(*(get_values(func, "test_hospital_publish")))
    def test_hospital_publish(self, value):
        '''
        获取机构的发布内容
        '''
        gmhttp.params.update({"hospital": self.hospital_id})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data', r.keys())
        self.assertIn('publish', r.get('data'))
        self.assertIn('offset', r.get('data'))
        if r.get('data').get('publish'):
            for item in r.get('data').get('publish'):
                self.assertIn('type', item.keys())
                self.assertIn('id', item.keys())
                self.assertIn('images', item.keys())
                self.assertIn('title', item.keys())
                self.assertIn(item.get('type'), ['free_activity', 'zhibo', 'article'])
                if item.get('type') == 'free_activity':
                    self.assertIn('status', item.keys())
                    self.assertIn(item.get('status'), [0, 1, 2])
                    self.assertIn('status_hint', item.keys())
                    self.assertIn('month', item.get('status_hint').keys())
                    # self.assertIn(item.get('status_hint').get('month'), range(1, 13))
                    self.assertIn('day', item.get('status_hint').keys())
                    # self.assertIn(item.get('status_hint').get('day'), range(1, 32))
                    self.assertIn('hour', item.get('status_hint').keys())
                    # self.assertIn(item.get('status_hint').get('hour'), range(1, 25))
                    self.assertIn('year', item.get('status_hint').keys())
                    # self.assertIn(item.get('status_hint').get('year'), range(1, 9999))
                    self.assertIn('participants', item.keys())
                    self.assertIsInstance(item.get('participants'), int)
                    self.assertIn('is_online', item.keys())
                    self.assertIn(item.get('is_online'), [0, 1])
                elif item.get('type') == 'zhibo':
                    self.assertIn('tags', item.keys())
                    self.assertIn('reply_num', item.keys())
                    self.assertIn('vote_num', item.keys())
                    self.assertIn('view_num', item.keys())
                    self.assertIn('live', item.keys())
                    self.assertIn('content', item.get('live'))
                    self.assertIn('source', item.get('live'))
                    self.assertIn('cover', item.get('live'))

                else:
                    self.assertIn('tags', item.keys())
                    self.assertIn('reply_num', item.keys())
                    self.assertIn('vote_num', item.keys())
                    self.assertIn('view_num', item.keys())

        # self.assertTrue(flag,msg='当前医院列表没有任何发布内容！')
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Hospital_Publish.run()
