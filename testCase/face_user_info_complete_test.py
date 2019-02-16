import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Face_User_Info_Complete(unittest.TestCase):
    '''
    用户信息采集
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.file_name = face_file_name_get()
        face_token_get(cls.file_name)

    @data(*(get_values(func, "test_face_user_info_complete")))
    @require_login
    def test_face_user_info_complete(self,value):
        '''
        用户信息采集
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


        data = {
            "birthday":'1999-01-01',
            "face_token":self.token,
            "gender":1,
            "tag_ids":[]
        }
        r = gmhttp.post(self.url,data=data).json()
        self.assertEqual(r.get("error"),0)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Face_User_Info_Complete.run()