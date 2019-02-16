from configparser import ConfigParser
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

sys.path.append(BASE_DIR)
c = ConfigParser()
c.read(os.path.join(BASE_DIR, "data"), encoding='utf-8')


class Gmei_config:
    def __init__(self):
        self._host = c.get('env_info', 'host')

    @property
    def host(self):
        if self._host.startswith('http'):
            return self._host
        return 'https://backend.igengmei.com'

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def hosts(self):
        return c.get('env_info', 'hosts').split(',')

    def api_name(self, o):
        return c.get('api_info', o)

    def body_params(self, o):
        return c.get('body_params', o)

    def get_info(self, s, o):
        return c.get(s, o)

    @property
    def android_params(self):
        # return dict(c.items('android_params'))
        return '&'.join([i[0] + '=' + i[1] for i in c.items('android_params')])

    def android_params_set(self, **kwargs):
        android_params = dict(c.items('android_params'), **kwargs)
        # return android_params
        return '&'.join([i + '=' + str(android_params[i]) for i in android_params])

    @property
    def ios_params(self):
        return '&'.join([i[0] + '=' + i[1] for i in c.items('ios_params')])

    def ios_params_set(self, **kwargs):
        android_params = dict(c.items('ios_params'), **kwargs)
        return '&'.join([i + '=' + str(android_params[i]) for i in android_params])

    def params(self, type="android"):
        if type == 'ios':
            return dict(c.items('ios_params'))
        elif type == "android":
            return dict(c.items('android_params'))
        else:
            raise AttributeError("Object '{}' has no attribute '{}'".format(self.__class__.__name__, type))

    def set(self, s, o, v):
        c.set(s, o, v)

    def edit(self):
        with open(os.path.join(BASE_DIR, "data"), 'w', encoding='utf-8') as f:
            c.write(f)


g = Gmei_config()
