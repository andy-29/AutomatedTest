import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
import random

@ddt
class Auto_Complete_Doctor(unittest.TestCase):
    '''
    医生自动补全
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_auto_complete_doctor")))
    def test_auto_complete_doctor(self, value):
        self._testMethodDoc = '医生自动补全，不指定医院'
        gmhttp.params.update(value.get('paramsdata'))
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        if r.get('data'):
            for item in r.get('data'):
                self.assertIn(value.get('paramsdata').get('q'), item.get('doctor_name'))

    @data(*(get_values(func, "test_auto_complete_doctor_hospital")))
    def test_auto_complete_doctor_hospital(self, value):
        self._testMethodDoc = '医生自动补全，指定医院'
        gmhttp.params.update(value.get('paramsdata'))
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        if r.get('data'):
            for item in r.get('data'):
                self.assertIn(value.get('paramsdata').get('q'), item.get('doctor_name'))


    def tearDown(self):
        pass


if __name__ == "__main__":
    Auto_Complete_Doctor.run()
