import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from common.id_for_test import *


@ddt
class Diary_Operation_Diary_Id(unittest.TestCase):
    '''
    日记本补充信息
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        cls.diary_id = diary_id_get()

    @data(*(get_values(func, "test_diary_operation_diary_id")))
    def test_diary_operation_diary_id(self, value):
        self._testMethodDoc = "--"
        '''
        获取日记本补充信息
        '''
        r = gmhttp.get(self.url.format(self.diary_id)).json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data', r.keys())
        self.assertIn('comment', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('comment'), dict)
        self.assertIn('bad', r.get('data').get('comment').keys())
        self.assertIsInstance(r.get('data').get('comment').get('bad'), list)
        self.assertIn('good', r.get('data').get('comment').keys())
        self.assertIsInstance(r.get('data').get('comment').get('good'), list)
        self.assertIn('rating', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('rating'), int)
        self.assertIn('service_name', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('service_name'), str)
        self.assertIn('hospital_env_rating', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('hospital_env_rating'), int)
        self.assertIn('doctor_name', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('doctor_name'), str)
        self.assertIn('pre_operation_image', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('pre_operation_image'), dict)
        self.assertIn('doctor_portrait', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('doctor_portrait'), str)
        self.assertIn('pre_operation_image_amount', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('pre_operation_image_amount'), str)
        self.assertIn('hospital_name', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('hospital_name'), str)
        # self.assertIn('diary_cover', r.get('data').keys())
        # self.assertIsInstance(r.get('data').get('diary_cover'), list)
        self.assertIn('operation_item_amount', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('operation_item_amount'), str)
        self.assertIn('pre_operation_images', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('pre_operation_images'), list)
        self.assertIn('operator_is_hospital_officer', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('operator_is_hospital_officer'), bool)
        self.assertIn('doctor_attitude_rating', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('doctor_attitude_rating'), int)
        self.assertIn('doctor_title', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('doctor_title'), str)
        self.assertIn('comment_count', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('comment_count'), int)
        self.assertIn('diary_title', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('diary_title'), str)
        self.assertIn('operation_effect_rating', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('operation_effect_rating'), int)
        self.assertIn('service_short_description', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('service_short_description'), str)
        self.assertIn('order_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('order_id'), str)
        self.assertIn('show_comment', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('show_comment'), bool)
        self.assertIn('price', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('price'), int)
        self.assertIn('order_info', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('order_info'), dict)
        self.assertIn('operation_timestamp', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('operation_timestamp'), int)
        self.assertIn('post_operation_image', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('post_operation_image'), dict)
        self.assertIn('operation_items', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('operation_items'), list)
        for item in r.get('data').get('operation_items'):
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), str)
            self.assertIn('tag_id', item.keys())
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
        self.assertIn('hospital_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('hospital_id'), str)
        self.assertIn('interval', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('interval'), str)
        self.assertIn('has_topics', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('has_topics'), bool)
        self.assertIn('service_image', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('service_image'), str)
        self.assertIn('service_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('service_id'), str)
        self.assertIn('doctor_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('doctor_id'), str)
        print('用例执行完毕!')

    def tearDown(self):
        # 删除日志
        pass

if __name__ == "__main__":
    Diary_Operation_Diary_Id.run()
