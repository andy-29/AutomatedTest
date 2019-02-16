import requests
import os
from copy import deepcopy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

sys.path.append(BASE_DIR)

from common.get_config import g
import time, re
import hashlib


def require_login(func):
    def _inner(*args, **kwargs):
        # sessionid = g.get_info('session', 'sessionid')
        # if sessionid:
        #     GmHttp().headers.update({"Cookie": "sessionid=" + sessionid})
        # else:
        cookie = gmhttp.headers.get('Cookie')
        if not cookie or cookie.find('sessionid') == -1:
            gmhttp.login()
        return func(*args, **kwargs)

    return _inner


class GmHttp:
    # user_agent = "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10"
    user_agent = "com.wanmeizhensuo.zhensuo/7.7.45 AsyncHttpClient/1.4.5 Android/9"

    def __init__(self, ostype='android', *args, **kwargs):
        self._type = ostype
        self._params = g.params(ostype)
        self.params = deepcopy(self._params)
        self.verify = False
        self.headers = {'User-Agent': GmHttp.user_agent}
        self._user = kwargs.get('user', g.get_info('user_info', 'telephone'))
        self._pwd = kwargs.get('pwd', g.get_info('user_info', 'password'))
        self.host = g.host
        self.uid = None

    def get(self, url, *args, **kwargs):
        rep = requests.get(url=url, params=self.params, headers=self.headers, verify=self.verify, **kwargs)
        return rep

    def post(self, url, *args, **kwargs):
        rep = requests.post(url=url, params=self.params, headers=self.headers, verify=self.verify, **kwargs)
        return rep

    def delete(self,url,*args,**kwargs):
        rep = requests.delete(url=url, params=self.params, headers=self.headers, verify=self.verify, **kwargs)
        return rep
    def reset(self):
        self.params = deepcopy(self._params)

    def login(self, usr=None, pwd=None):
        # 下面全是服务于登录
        if self._type == 'android':
            device_info = g.get_info('android_params', 'device_id')
        elif self._type == 'ios':
            device_info = g.get_info('ios_params', 'device_id')
        else:
            raise AttributeError('params必须为android_params或ios_params')

        salt = g.get_info('env_info', 'salt')
        ts = str(int(time.time()))

        # 获取_gm_token
        _gm_token = hashlib.md5((device_info + ts + salt).encode()).hexdigest()[6:12] + ts
        self.headers.update({
            'Cookie': '_gm_token=' + _gm_token
        })
        phone = usr if usr else self._user
        password = pwd if pwd else self._pwd
        rep = self.post(
            url=self.host + '/api/accounts/login/password',
            data={'phone': phone, 'password': password}
        )
        try:
            return rep.json()
        except:
            pass
        finally:
            if rep.json().get('error') == 0:
                self.uid = rep.json().get('data').get('user_id')
                sessionid = re.search(r'sessionid=(\w+);.*', rep.headers.get('Set-Cookie')).groups()
                if sessionid:
                    self.headers.update({"Cookie": "sessionid=" + sessionid[0]})
                    # g.set('session', 'sessionid', sessionid[0])
                    # g.edit()


gmhttp = GmHttp()
