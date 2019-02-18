import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Report_Info(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_report_info")))
    @require_login
    def test_report_info(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        service_id, hospital_id, doctor_id,_ = service_id_get()
        gmhttp.params.update({"doctor_id":doctor_id,"hospital_id":hospital_id,"service_id":service_id})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Report_Info.run()