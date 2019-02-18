import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Hospital_Album(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        _,cls.hospital_id,*_ = service_id_get()
    @data(*(get_values(func, "test_hospital_album")))
    def test_hospital_album(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        gmhttp.params.update({"hospital_id":self.hospital_id})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIn('pic',r['data'].keys())
        if r.get('data').get('pic'):
            for item in r.get('data').get('pic'):
                self.assertIn('pic',item.keys())
                self.assertIn('is_video',item.keys())
                self.assertIn('name',item.keys())
                self.assertIn('video_url',item.keys())
                self.assertIn('pic_w',item.keys())

        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Hospital_Album.run()