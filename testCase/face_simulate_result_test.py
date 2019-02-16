import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Face_Simulate_Result(unittest.TestCase):
    '''
    上传分析结果
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.file_name = face_file_name_get()
        face_token_get(cls.file_name)

        # 以上代码是为了防止 初始环境下没有分析报告





    @data(*(get_values(func, "test_face_simulate_result")))
    @require_login
    def test_face_simulate_result(self,value):
        '''
        上传分析结果
        '''


        num = 0
        while num < 5:
            time.sleep(6)
            url = g.host + g.get_info('api_info', 'face_latest_analyze_result')
            r = gmhttp.get(url).json()
            if r.get('error') != 0:
                num += 1
                continue
            break
        self.assertEqual(r.get("error"), 0)
        self.assertNotEqual(5, num, msg='30秒内没有获取面部分析报告！')
        self.token = r.get('data').get('token')
        r = gmhttp.post(self.url,data={"file_name": self.file_name, "token": self.token,"type":1}).json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data', r.keys())
        self.assertIn('city_tag_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('city_tag_id'), str)
        self.assertIn('saved', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('saved'), bool)
        self.assertIn('share_data', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('share_data'), dict)
        self.assertIn('qq', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('qq'), dict)
        self.assertIn('weibo', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('weibo'), dict)
        self.assertIn('url', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('url'), str)
        self.assertIn('image', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('image'), str)
        self.assertIn('wechatmini', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('wechatmini'), dict)
        self.assertIn('wechat', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('wechat'), dict)
        self.assertIn('wechatline', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('wechatline'), dict)
        self.assertIn('tag_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('tag_id'), int)
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Face_Simulate_Result.run()
