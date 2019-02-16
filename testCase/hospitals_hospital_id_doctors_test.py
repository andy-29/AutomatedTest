import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Hospitals_Doctors(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        _, cls.hospital_id, *_ = service_id_get()
    @data(*(get_values(func, "test_hospitals_hospital_id_doctors")))
    def test_hospitals_hospital_id_doctors(self,value):
        '''
        
        '''
        r = gmhttp.get(self.url.format(self.hospital_id)).json()
        self.assertIs(0,r.get('error'))
        for item in r.get('data'):
            self.assertIn('star', item.keys())
            self.assertIsInstance(item.get('star'), float)
            self.assertIn('title', item.keys())
            self.assertIsInstance(item.get('title'), str)
            self.assertIn('working_year', item.keys())
            self.assertIsInstance(item.get('working_year'), int)
            self.assertIn('doctor_name', item.keys())
            self.assertIsInstance(item.get('doctor_name'), str)
            self.assertIn('good_at', item.keys())
            self.assertIsInstance(item.get('good_at'), list)
            self.assertIn('portrait', item.keys())
            self.assertIsInstance(item.get('portrait'), str)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), str)


    def tearDown(self):
        pass


if __name__ == "__main__":
    Hospitals_Doctors.run()