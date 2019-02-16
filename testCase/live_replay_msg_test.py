import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Live_Replay_Msg(unittest.TestCase):
    '''
    弹幕回放
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_live_replay_msg")))
    def test_live_replay_msg(self,value):
        '''
        弹幕回放
        '''
        # 获取topic列表
        uri = g.get_info('api_info', 'live_list')
        url = self.host + uri
        r = gmhttp.get(url).json()
        self.assertEqual(r.get("error"), 0)
        topic_list = map(lambda x: x.get('topic_id'), filter(lambda x: x.get('status') == 0, r.get('data')))

        for topic_id in topic_list:
            gmhttp.params.update({"topic_id": topic_id})
            r = gmhttp.get(self.url).json()
            gmhttp.reset()
            self.assertEqual(r.get("error"), 0)
            self.assertIn('data', r.keys())
            for item in r.get('data').values():
                for sub_item in item:
                    self.assertIn('text', sub_item.keys())
                    self.assertIsInstance(sub_item.get('text'), str)
                    self.assertIn('type', sub_item.keys())
                    self.assertIsInstance(sub_item.get('type'), int)
                    self.assertIn('id', sub_item.keys())
                    self.assertIsInstance(sub_item.get('id'), int)
                    self.assertIn('name', sub_item.keys())
                    self.assertIsInstance(sub_item.get('name'), str)
            break
        print('用例执行完毕!')

    def tearDown(self):
        pass

        # 关掉直播
        # finish_zb = g.get_info('api_info', 'live_finish')
        # url = self.host + finish_zb + "?" + self.android_params
        # r = gmhttp.post(url, verify=False, headers=self.header, data={"channel_id": self.channel})
        # self.assertEqual(r.status_code, 200, '返回码不为200！')
        # r = r.json()
        # self.assertEqual(r.get("error"), 0)


if __name__ == "__main__":
    Live_Replay_Msg.run()
