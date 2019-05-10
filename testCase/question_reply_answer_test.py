import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Question_Reply_Answer(unittest.TestCase):
    '''
    创建回答评论
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.answer_id = 645785
        # cls.answer_id = answer_id_get()

    @data(*(get_values(func, "test_question_reply_answer")))
    @require_login
    def test_question_reply_answer(self,value):
        self._testMethodDoc = "创建回答评论"
        '''
        创建回答评论
        '''
        #,这个answer_id是从/hybrid/question/answer_list/_data?question_id=
        import time
        time.sleep(random.choice(range(10,20)))
        post_data = {'answer_id': self.answer_id, 'content': '开心{}'.format(random.choice(['啊','哈','了']))}
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Question_Reply_Answer.run()