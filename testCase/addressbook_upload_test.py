import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Addressbook_Upload(unittest.TestCase):
    '''
    上传通讯录
    '''
    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func,"test_addressbook_upload")))
    @require_login
    def test_addressbook_upload(self,value):
        self._testMethodDoc = '上传通讯录'
        gmhttp.headers.update({"Content-Type":'application/x-www-form-urlencoded'})
        r = gmhttp.post(self.url, json=value.get("requestdata")).json()
        gmhttp.headers.pop("Content-Type")
        self.assertEqual(r, value.get('assertdata'))

    @data(*(get_values(func, "test_addressbook_upload_null")))
    @require_login
    def test_addressbook_upload_null(self,value):
        self._testMethodDoc = '上传空通讯录'
        gmhttp.headers.update({"Content-Type": 'application/x-www-form-urlencoded'})
        r = gmhttp.post(self.url, json=value.get("requestdata")).json()
        gmhttp.headers.pop("Content-Type")
        self.assertEqual(r, value.get('assertdata'))

    def tearDown(self):
        pass


if __name__ == "__main__":
    Addressbook_Upload.run()
