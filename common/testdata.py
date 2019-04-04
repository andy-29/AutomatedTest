import requests
import sys
import sqlite3
from common.get_config import g

'''
我们的配置均在库里面进行维护，使用同机器下接口访问
1.为了防止接口服务未启动，需要做额外处理，直接对库进行读写
'''


def get_values(func, casname):
    r = None
    try:
        r = requests.get('http://127.0.0.1:8090/searchcasedata/', params={"func": func, 'case': casname}).json()
    except Exception:
        '''
        异常不处理
        '''
    if r:
        values = [{"uridata": item.get('uridata'),
                   "paramsdata": eval(item.get('paramsdata')) if item.get('paramsdata') else {},
                   "requestdata": eval(item.get('requestdata')) if item.get('requestdata') else {},
                   "assertdata": eval(item.get('assertdata')) if item.get('assertdata') else {}} for item in r]
    else:
        # 直接在数据库获取--防止服务挂掉
        if sys.platform == "darwin":
            _path = g.get_info('env_info', 'database_path_mac')
        else:
            _path = g.get_info('env_info', 'database_path_linux')
        try:
            s = sqlite3.connect(_path)
        except sqlite3.OperationalError:
            _path = g.get_info('env_info', 'database_path_aliyun')
            s = sqlite3.connect(_path)
        sc = s.cursor()
        rep = sc.execute(
            'SELECT td.uridata,td.paramsdata,td.requestdata,td.assertdata FROM gmapi_testdata td,gmapi_apistatus ta WHERE td.`case` = "%s" AND td.uri_id = ta.id AND ta.func = "%s"' % (
            casname, func)).fetchall()
        values = [{"uridata": item[0], "paramsdata": eval(item[1]) if item[1] else {},
                   "requestdata": eval(item[2]) if item[2] else {},
                   "assertdata": eval(item[3]) if item[3] else {}} for item in rep]
        s.close()
    return values if values else  [{"uridata": '', "paramsdata": '',"requestdata": {}, "assertdata": {}}]
