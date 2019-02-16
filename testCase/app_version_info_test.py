import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *

@ddt
class App_Version_Info(unittest.TestCase):
    '''
    检查app是否更新
    '''

    @classmethod
    def setUpClass(cls):
        print('获取环境信息和接口信息')
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.lasted_version = cls._lasted_version

    @data(*(get_values(func,"test_app_version_info_lower")))
    def test_app_version_info_lower(self,value):
        self._testMethodDoc = '统计新用户接口'

        params_version = '.'.join([str(int(i) -1) for i in self.lasted_version.split('.') if int(i)>1])
        gmhttp.params.update({'version':params_version})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        # self.assertEqual(r.status_code, 200, '返回码不为200！')
        # r = r.json()
        self.assertIn('data', r.keys())
        self.assertEqual(r.get('error'),0)
        #
        # self.assertIn('version',r.get('data').keys())
        # self.assertIn('source',r.get('data').keys())
        # self.assertIn('version_code',r.get('data').keys())
        # self.assertIn('apk',r.get('data').keys())
        # self.assertIn('create_time',r.get('data').keys())
        # self.assertIn('minimum_support_version',r.get('data').keys())
        # self.assertIn('description',r.get('data').keys())
        # print('用例执行完毕!')

    @data(*(get_values(func,"test_app_version_info_higher")))
    def test_app_version_info_higher(self,value):
        self._testMethodDoc = '当前版本高检查app是否更新'
        params_version = '.'.join([str(int(i) +1) for i in self.lasted_version.split('.') if int(i)>1])
        gmhttp.params.update({'version':params_version})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertIn('data', r.keys())
        self.assertEqual(r.get('error'),1)
        self.assertEqual(r.get('message'),"已经是最新版本了!")
        #
        # self.assertIn('version',r.get('data').keys())
        # self.assertIn('source',r.get('data').keys())
        # self.assertIn('version_code',r.get('data').keys())
        # self.assertIn('apk',r.get('data').keys())
        # self.assertIn('create_time',r.get('data').keys())
        # self.assertIn('minimum_support_version',r.get('data').keys())
        # self.assertIn('description',r.get('data').keys())
        # print('用例执行完毕!')

    @data(*(get_values(func,"test_app_version_info_equal")))
    def test_app_version_info_equal(self,value):
        self._testMethodDoc = '版本相同检查app是否更新'
        gmhttp.params.update({'version':self.lasted_version})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        #
        self.assertIn('data', r.keys())
        self.assertEqual(r.get('error'),1)
        self.assertEqual(r.get('message'),"已经是最新版本了!")
        #
        # self.assertIn('version',r.get('data').keys())
        # self.assertIn('source',r.get('data').keys())
        # self.assertIn('version_code',r.get('data').keys())
        # self.assertIn('apk',r.get('data').keys())
        # self.assertIn('create_time',r.get('data').keys())
        # self.assertIn('minimum_support_version',r.get('data').keys())
        # self.assertIn('description',r.get('data').keys())
        # print('用例执行完毕!')


    @property
    def _lasted_version(self):
        '''
        检查app是否更新
        '''

        r = gmhttp.get(self.url).json()
        # 查看返回的最新版本号
        lasted_version = r.get('data').get('version')
        return lasted_version

    def tearDown(self):
        gmhttp.reset()


if __name__ == "__main__":
    App_Version_Info.run()
