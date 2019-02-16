import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Face_Analyze(unittest.TestCase):
    '''
    人脸分析接口
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.file_name = face_file_name_get()

    @data(*(get_values(func, "test_face_analyze")))
    @require_login
    def test_face_analyze(self, value):
        '''
        人脸分析接口
        '''
        r = gmhttp.post(self.url, data={"filename": self.file_name}).json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data', r.keys())
        self.assertIn('token', r.get('data').keys())
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Face_Analyze.run()
