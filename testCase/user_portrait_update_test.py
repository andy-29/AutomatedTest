import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_Portrait_Update(unittest.TestCase):
    '''
    修改头像接口
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_user_portrait_update")))
    @require_login
    def test_user_portrait_update(self,value):
        '''
        修改头像接口
        '''
        # 先上传图片,图片放在conmmon下
        with open(os.path.join(BASE_DIR, 'common', 'test.jpg'), 'rb') as f:
            info = f.read()
        files = {"portrait": ('portrait', info, 'image/jpg')}   #key值需要和抓包相同
        r = gmhttp.post(self.url, files=files).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('portrait', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('portrait'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    User_Portrait_Update.run()