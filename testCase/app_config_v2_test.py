import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class App_Config_V2(unittest.TestCase):
    '''
    app打开拉取信息
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_app_config_v2")))
    def test_app_config_v2(self,value):
        '''
        app打开拉取信息
        '''
        self._testMethodDoc = '配置信息'
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data', r.keys())
        self.assertIn('search_placeholder', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('search_placeholder'), str)
        self.assertIn('is_tab_hit', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_tab_hit'), bool)
        self.assertIn('home_7695_is_gray', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('home_7695_is_gray'), bool)
        self.assertIn('is_homev6', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_homev6'), bool)
        self.assertIn('is_content_search', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_content_search'), bool)
        self.assertIn('show_ad', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('show_ad'), bool)
        self.assertIn('force_update', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('force_update'), bool)
        self.assertIn('is_service_hit', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_service_hit'), bool)
        self.assertIn('greeting', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('greeting'), dict)
        self.assertIn('url', r.get('data').get('greeting').keys())
        self.assertIsInstance(r.get('data').get('greeting').get('url'), str)
        self.assertIn('image', r.get('data').get('greeting').keys())
        self.assertIsInstance(r.get('data').get('greeting').get('image'), str)
        self.assertIn('id', r.get('data').get('greeting').keys())
        self.assertIsInstance(r.get('data').get('greeting').get('id'), int)
        self.assertIn('show_selected_apps', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('show_selected_apps'), bool)
        self.assertIn('is_hit_org_home_gray', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_hit_org_home_gray'), bool)
        self.assertIn('tab_config', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('tab_config'), list)
        self.assertIn('sign_status', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('sign_status'), bool)
        self.assertIn('current_version', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('current_version'), dict)
        self.assertIn('version', r.get('data').get('current_version').keys())
        self.assertIsInstance(r.get('data').get('current_version').get('version'), str)
        self.assertIn('source', r.get('data').get('current_version').keys())
        self.assertIsInstance(r.get('data').get('current_version').get('source'), int)
        self.assertIn('version_code', r.get('data').get('current_version').keys())
        self.assertIsInstance(r.get('data').get('current_version').get('version_code'), int)
        self.assertIn('apk', r.get('data').get('current_version').keys())
        self.assertIsInstance(r.get('data').get('current_version').get('apk'), str)
        self.assertIn('create_time', r.get('data').get('current_version').keys())
        self.assertIsInstance(r.get('data').get('current_version').get('create_time'), str)
        self.assertIn('minimum_support_version', r.get('data').get('current_version').keys())
        self.assertIsInstance(r.get('data').get('current_version').get('minimum_support_version'), str)
        self.assertIn('desc', r.get('data').get('current_version').keys())
        self.assertIsInstance(r.get('data').get('current_version').get('desc'), str)
        self.assertIn('description', r.get('data').get('current_version').keys())
        self.assertIsInstance(r.get('data').get('current_version').get('description'), str)
        self.assertIn('type', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('type'), int)
        self.assertIn('is_search', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_search'), bool)
        self.assertIn('has_search_knowledge_tab', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('has_search_knowledge_tab'), bool)
        self.assertIn('is_face_user_info_complete', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_face_user_info_complete'), bool)
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    App_Config_V2.run()
