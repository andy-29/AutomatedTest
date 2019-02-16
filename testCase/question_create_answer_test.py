import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Question_Create_Answer(unittest.TestCase):
    '''
    创建问答回复
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.question_id,_ = question_id_get()


    @data(*(get_values(func, "test_question_create_answer")))
    @require_login
    def test_question_create_answer(self,value):

        gmhttp.params.update({"release":1})
        post_data = {'content': '[{"type":0,"content":"恢复好又美美哒了吧？"}]',
                     'question_id': self.question_id}  # '211348'
        r = gmhttp.post(self.url, data=post_data).json()
        gmhttp.reset()
        # pprint(r.content.decode())
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Question_Create_Answer.run()
