import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Report_Upload(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_report_upload")))
    @require_login
    def test_report_upload(self, value):
        '''
        
        '''
        f = open(os.path.join(BASE_DIR, 'common', 'test.jpg'), 'rb')
        files = {'report': ('report', f), 'type': ('type', 'image'), 'file': ('file', 'file')}
        r = gmhttp.post(url=g.host + '/files/upload/', files=files).json()
        f.close()
        out_file = r['data']['file']
        service_id, hospital_id, doctor_id = service_id_get()
        post_data = {'content': "不错哦",
                     'doctor_id': doctor_id,
                     'hospital_id': hospital_id,
                     'images': '[{"image": "' + out_file + '"}]',
                     'service_id' :service_id }

        r = gmhttp.post(self.url,
                        data=post_data)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Report_Upload.run()
