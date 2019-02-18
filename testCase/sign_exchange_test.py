import gmhttp
import unittest
import os
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
class Sign_Exchange(unittest.TestCase):
    '''
    签到兑换礼品
    1.积分（连续签到天数）足够，礼品有剩余，兑换成功
    2.积分（连续签到天数）足够，礼品不足，兑换失败
    3.积分不足，兑换失败
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
        from common.getcookie import create_header
        self.header = create_header(self.user_telephone, self.password, 'android_params').get('header')
        self.assertTrue(self.header, msg='登录未成功！')

        #通过签到详情页获取prize
        url = self.host + g.get_info('api_info','sign_detail')+ "?" + self.android_params
        r = gmhttp.get(url,headers=self.header,verify = False).json()
        self.act_id = r.get('data').get('id')
        self.last_days = r.get('data').get('last_days')
        self.prizes = [(item.get('id'),item.get('exchange_days')) for item in r.get('data').get('prizes')]

    @data(*(get_values(func, "test_sign_exchange")))
    def test_sign_exchange(self,value):
        self._testMethodDoc = "--"
        '''
        签到兑换礼品
        '''
        #获取兑换要求小于last_days的礼品
        low_list = [item[0] for item in self.prizes if item[1] <= self.last_days]
        up_list = [item[0] for item in self.prizes if item[1] > self.last_days]
        prize_id = up_list[0] if len(up_list) else None
        if prize_id:
            print('执行兑换不成功分支！')
            data = {
                'activity_id':self.act_id,
                'prize_id':prize_id,
                'count':1
            }
            url = self.host + self.api_name+ "?" + self.android_params
            r = gmhttp.post(url,verify=False,data=data,headers =self.header)
            self.assertEqual(r.status_code,200,'返回码不为200！')
            r = r.json()
            self.assertEqual(r.get("error"),1)
            self.assertEqual(r.get('message'), '对不起，未到兑换门槛')
        prize_id = low_list[0] if len(low_list) else None
        if prize_id:
            print('执行兑换成功分支！')
            data = {
                'activity_id':self.act_id,
                'prize_id':prize_id,
                'count':1
            }
            url = self.host + self.api_name+ "?" + self.android_params
            r = gmhttp.post(url,verify=False,data=data,headers =self.header)
            self.assertEqual(r.status_code,200,'返回码不为200！')
            r = r.json()
            self.assertEqual(r.get("error"),0)
            self.assertEqual(r.get("message"),'兑换成功')
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Sign_Exchange.run()