import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Expert_Accept_Call(unittest.TestCase):
    '''
    当前时间医生或机构是否接电话
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        cls.service_id, cls.hospital_id, cls.doctor_id,_ = service_id_get()
    @data(*(get_values(func, "test_expert_accept_call")))
    @require_login
    def test_expert_accept_call(self,value):
        self._testMethodDoc = "--"
        '''
        当前时间医生或机构是否接电话
        '''


        gmhttp.params.update({"organization_id":self.hospital_id,"expert_id":self.doctor_id})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIsInstance(r.get('data').get('accept_call'),bool)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Expert_Accept_Call.run()