from datetime import *
import unittest
from unittest.suite import TestSuite
from BeautifulReport import BeautifulReport
import shutil
from common.get_config import g
import requests
import json
import sqlite3
import sys
import copy
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#
# def all_func(flag=None):
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
#     if flag:
#         rep = sc.execute(
#             'SELECT ga.func FROM gmapi_apistatus ga  left join gmapi_apistatus_env gae on ga.id = gae.apistatus_id WHERE envhost_id =2').fetchall()
#     else:
#         rep = sc.execute('SELECT func FROM gmapi_apistatus WHERE status_id=1 AND usestatus_id=1').fetchall()
#     _a = [item[0] for item in rep]
#     s.close()
#     return _a


def run_test(path: str = 'testCase'):
    """
    :param path: With default path testcase, the method will execute all testcases, otherwise it only execute the
    cases which in the specific path
    :return: test report
    """

    host = g.host
    testsuits = TestSuite()

    report_name = "{}_{}".format(path, str(datetime.now().strftime("%Y%m%d%H%M%S")))
    if host == "https://backend.igengmei.com":
        copyname = 'testReport/igengmei_test_api_ressult.html'
    else:
        copyname = 'testReport/test_api_ressult.html'
    # 保证连接正常，testdata做了断网简单兼容，此处也做兼容
    try:
        a = requests.get('http://127.0.0.1:8090/testapi/checkedapi/', params={'env': host}).json()
        with open(case_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(a))
    except Exception:
        with open(case_file, 'r', encoding='utf-8') as f:
            _data = f.read()
        a = eval(_data)
    _a = copy.deepcopy(a)
    for case in a:
        _unit = unittest.defaultTestLoader.discover(path, pattern=case + '_test.py', top_level_dir='testCase')
        if _unit:
            testsuits.addTest(_unit)
            _a.remove(case)

    result = BeautifulReport(testsuits)
    result.report(filename=report_name, description="API接口", log_path='testReport')
    shutil.copy('testReport/%s.html' % report_name, copyname)

    result_list = [item for item in result.result_list if item[4] != '成功']
    # 我们需要获取已经记录但是没有写脚本的接口和case,收录在_a中

    from PIL import Image, ImageDraw, ImageFont

    length, weight_unit = 1000, 20
    back_img = Image.new(mode='RGB', size=(length, weight_unit * ((len(result_list) or 1) + len(_a) + 2)),
                         color=(255, 255, 255))
    draw_img = ImageDraw.ImageDraw(back_img)
    font = ImageFont.truetype('arial.ttf', size=weight_unit, encoding='gbk')

    num = 0
    if len(result_list) == 0:
        draw_img.text((0, weight_unit * num), '全部通过', font=font, fill='green')
        num += 1
    for item in result_list:
        draw_img.text((0, weight_unit * num), item[0] + ':' + item[1], font=font, fill='red')
        num += 1
    if _a:
        draw_img.text((0, weight_unit * num), 'The following interface scripts are missing！！', font=font,
                      fill='red')
        num += 1
        for item in _a:
            draw_img.text((0, weight_unit * num), item, font=font, fill='blue')
            num += 1
    back_img.save('testReport/error.jpg')


if __name__ == "__main__":
    import os

    usr_dir = os.path.expanduser('~')
    case_file = os.path.join(usr_dir, 'case.txt')

    os.remove('testReport/error.jpg') if os.path.exists('testReport/error.jpg') else None

    run_test()
