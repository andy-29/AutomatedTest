import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from common.id_for_test import *
@ddt
class Diary_Add_Preoperation_Images(unittest.TestCase):
    '''
    增加术前照片
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.diary_id = diary_id_get()
        cls.file_name = file_name_get()

    @data(*(get_values(func, "test_diary_add_preoperation_images")))
    @require_login
    def test_diary_add_preoperation_images(self,value):
        self._testMethodDoc = "--"
        '''
        增加术前照片
        '''
        data = {
            'diary_id':self.diary_id,
            'images':'["{}"]'.format(self.file_name)
        }
        r = gmhttp.post(self.url,data=data).json()
        self.assertEqual(r.get("error"),0)

    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Add_Preoperation_Images.run()