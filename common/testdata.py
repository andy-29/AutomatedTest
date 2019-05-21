import requests
import sys
import sqlite3
from common.get_config import g
import os
import json

'''
我们的配置均在库里面进行维护，使用同机器下接口访问
1.为了防止接口服务未启动，需要做额外处理，直接对库进行读写
'''
usr_dir = os.path.expanduser('~')
st_file = os.path.join(usr_dir, 'unittest.txt')
mode = 'r' if os.path.exists(st_file) else 'w'
with open(st_file, mode, encoding='utf-8'):
    ''
#先更新所有配置
try:
    er = requests.get('http://127.0.0.1:8090/testapi/envdata',timeout=3).json()
    dr = requests.get('http://127.0.0.1:8090/testapi/allcasedata',timeout=3).json()
    with open(st_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps([er,dr]))
except Exception:
    pass

def get_values(func, casname):
    r = None
    er = {}
    values = []
    host = g.host
    if host == "http://backend.pre.igengmei.com":
        host = "https://backend.igengmei.com"
    try:
        values = requests.get('http://127.0.0.1:8090/testapi/searchcasedata',timeout=3,
                              params={"func": func, 'case': casname, 'env': host}).json()
        #进行数据拜正
        for item in values:
            item['paramsdata'] = eval(item['paramsdata'] or '{}')
            item['requestdata'] = eval(item['requestdata'] or '{}')
            item['assertdata'] = eval(item['assertdata'] or '{}')
    except Exception:
        '''
        希望不要跑到这里
        在本地磁盘里里拿取，存在工程外的地方~~~     用户根目录，可能存在误删，不怕~
        '''
        # 全部取出来，更新还需要存进去，维护在unittest.txt的index1
        with open(st_file, 'r', encoding='utf-8') as f:
            st_info = f.read()
            st_dict = json.loads(st_info)
            _dict = eval(st_dict[1].get(casname))
            values = _dict.get(str(st_dict[0].get(host)))

    finally:
        return values or [{"uridata": '', "paramsdata": '', "requestdata": {}, "assertdata": {}}]
    ###移除直接读取数据库，保证8090端口起服务
    # else:
    #     # 直接在数据库获取--防止服务挂掉
    #     if sys.platform == "darwin":
    #         _path = g.get_info('env_info', 'database_path_mac')
    #     else:
    #         _path = g.get_info('env_info', 'database_path_linux')
    #     try:
    #         s = sqlite3.connect(_path)
    #     except sqlite3.OperationalError:
    #         _path = g.get_info('env_info', 'database_path_aliyun')
    #         s = sqlite3.connect(_path)
    #     sc = s.cursor()
    #     rep = sc.execute(
    #         'SELECT td.totaldata,td.paramsdata,td.requestdata,td.assertdata FROM gmapi_testdata td,gmapi_apistatus ta WHERE td.`case` = "%s" AND td.uri_id = ta.id AND ta.func = "%s"' % (
    #         casname, func)).fetchall()
    #     values = [{"uridata": item[0], "paramsdata": eval(item[1]) if item[1] else {},
    #                "requestdata": eval(item[2]) if item[2] else {},
    #                "assertdata": eval(item[3]) if item[3] else {}} for item in rep]
    #     s.close()


if __name__ == '__main__':
    d = get_values('account_login_phone', 'test_account_login_phone_errorTel')
