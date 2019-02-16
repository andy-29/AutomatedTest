import requests
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

sys.path.append(BASE_DIR)
from common.get_config import g


class Live:
    '''
    直播相关
    '''
    def __init__(self):
        self.host = g.host
        self.android_params = g.android_params
        user_telephone = g.get_info('user_info', 'telephone')
        password = g.get_info('user_info', 'password')
        from common.getcookie import create_header
        self.header = create_header(user_telephone, password, 'android_params').get('header')

    def create_live(self):
        url = self.host + '/files/upload/' + "?" + self.android_params
        with open(os.path.join(BASE_DIR, 'common', 'test.jpg'), 'rb') as f:
            info = f.read()
        files = {"file": ('test.jpg', info, 'image/jpg')}
        r = requests.post(url, files=files, headers=self.header, verify=False)
        self.file_name = r.json().get('data').get('file')

        push_live = g.get_info('api_info', 'live_push_live_info')
        tag_id = g.get_info('env_info', 'tag_id1')
        url = self.host + push_live + "?" + 'title={}&cover_url={}&tag_id={}'.format('直播测试',
                                                                                     self.file_name,
                                                                                     tag_id) + '&' + self.android_params
        r = requests.get(url, verify=False, headers=self.header)
        r = r.json()
        self.channel = r.get('data').get('channel')
        return  self.channel

    def get_live(self):
        url = self.host + g.get_info('api_info','index_v6')
        params = g.params()
        params.update({'tabtype':'live'})
        r = requests.get(url,params=params,verify=False).json()
        d_live = r.get('data').get('data_live')
        dlive_list = [item.get('topic_id') for item in d_live if item['status'] in [0,1]]
        return dlive_list[0] if dlive_list else None


lobj = Live()