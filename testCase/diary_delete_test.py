import gmhttp
import unittest
import os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(BASE_DIR)
from common.get_config import g





import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Diary_Delete(unittest.TestCase):
    '''
    删除日记本
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        print('获取环境信息和接口信息')
        self.host = g.host
        self.api_name = g.api_name(os.path.basename(__file__).split('_test.py')[0])
        self.android_params = g.android_params

        self.user_telephone = g.get_info('user_info', 'telephone')
        self.password = g.get_info('user_info', 'password')
        # 直接使用getcookie的create_header函数，返回内容不为空则此脚本成功
        from common.getcookie import create_header
        self.header = create_header(self.user_telephone, self.password, 'android_params').get('header')
        self.assertTrue(self.header, msg='登录未成功！')
        # 首先先创建日记
        # 日记接口
        api_step1 = g.get_info('api_info', 'diary_additional_info_v1')
        url = self.host + api_step1 + "?" + self.android_params
        self.tag_id1 = g.get_info('env_info', 'tag_id1')
        r = gmhttp.post(url, data={
            'tag_ids': '[{}]'.format(self.tag_id1),
            'operation_timestamp': int(time.time()),
            'cover': '',
            'images': []
        },
                          headers=self.header,
                          verify=False)
        r = r.json()
        self.assertEqual(0, r.get('error'), msg='创建前提日记本失败！')
        self.diary_id = r.get('data').get('id')
    @data(*(get_values(func, "test_diary_delete")))
    def test_diary_delete(self,value):
        self._testMethodDoc = "--"
        '''
        删除日记本
        '''
        data = {
            'diary_id':self.diary_id
        }
        url = self.host + self.api_name+ "?" + self.android_params
        r = gmhttp.post(url,verify=False,data=data,headers =self.header)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertEqual(r.get("message"),'删除成功')
        self.assertIn('data',r.keys())
        self.assertTrue(r.get('data').get('has_deleted'))
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Delete.run()