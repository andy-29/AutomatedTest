import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Face_Questions(unittest.TestCase):
    '''
    用户信息采集问题
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_face_questions")))
    def test_face_questions(self,value):
        self._testMethodDoc = "--"
        '''
        用户信息采集问题
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('answer_two', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('answer_two'), list)
        for item in r.get('data').get('answer_two'):
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('value', item.keys())
            self.assertIsInstance(item.get('value'), str)
        self.assertIn('question_two', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('question_two'), str)
        self.assertIn('question_one', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('question_one'), str)
        self.assertIn('answer_one', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('answer_one'), list)
        for item in r.get('data').get('answer_one'):
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('value', item.keys())
            self.assertIsInstance(item.get('value'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Face_Questions.run()