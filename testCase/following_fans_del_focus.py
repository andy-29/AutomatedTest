from common.common import back_domain
from copy import deepcopy
import unittest
import requests
from pprint import pprint


class Del_Focus(unittest.TestCase):
    """个人中心，我的关注，取消关注"""
    def test_del_focus(self):
        inner_data = deepcopy()
        r = requests.post(url=back_domain,params=)
        # dict_json = json.loads(r.content.decode())
        pprint(r.content.decode())
        # self.assertEqual(0, dict_json['error'])


if __name__ == '__main__':
    Del_Focus.run()
