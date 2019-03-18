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

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def all_func(flag=None):
    if sys.platform == "win32":
        _path = g.get_info('env_info', 'database_path_windows')
    else:
        _path = g.get_info('env_info', 'database_path_linux')
    s = sqlite3.connect(_path)
    sc = s.cursor()
    if flag:
        rep = sc.execute(
            'SELECT ga.func FROM gmapi_apistatus ga  left join gmapi_apistatus_env gae on ga.id = gae.apistatus_id WHERE envhost_id =2').fetchall()
    else:
        rep = sc.execute('SELECT func FROM gmapi_apistatus WHERE status_id=1 AND usestatus_id=1').fetchall()
    _a = [item[0] for item in rep]
    s.close()
    return _a


def run_test(path: str = 'testCase'):
    """
    :param path: With default path testcase, the method will execute all testcases, otherwise it only execute the
    cases which in the specific path
    :return: test report
    """

    # if path == 'testCase':
    #     for dir in os.listdir(os.path.join(os.curdir, path)):
    #         if os.path.isdir(dir):
    #             testsuits.addTests(unittest.defaultTestLoader.discover(dir, pattern='*test.py', top_level_dir='testCase'))
    # testsuits.addTests(unittest.defaultTestLoader.discover(path, pattern='*test.py', top_level_dir='testCase'))
    from common.getcookie import gmhttp
    # 更新cookie：对common.py的第一行json传进行修改，后期再整合
    # # 为了兼容取cookie的方式，这里对common.py文件进行修改
    # if host == "https://backend.igengmei.com":
    #     usr, pwd = '+8618311429100', '123456'
    # else:
    #     usr, pwd = '+8613810269337', 'Ww850201jsct'
    # dct = create_header(usr, pwd, params='ios_params', force=True)
    # with open(r'common/common.py', 'r+', encoding='utf-8') as f:
    #     fr = f.readlines()
    # fr[0] = 'cookies = {"sessionid": "%s"}\n' % dct.get("sessionId")
    # fr[3] = 'back_end_domain = "{}"\n'.format(host)
    # with open(r'common/common.py', 'w', encoding='utf-8') as f:
    #     f.writelines(fr)
    # # ========================================================

    host = g.host
    testsuits = TestSuite()

    report_name = "{}_{}".format(path, str(datetime.now().strftime("%Y%m%d%H%M%S")))
    if host == "https://backend.igengmei.com":
        copyname = 'testReport/igengmei_test_api_ressult.html'
        try:
            a = requests.get('http://127.0.0.1:8090/checkedapi/', params={'env': host}).json()
        except Exception:
            '''
            异常时直接操作库
            '''
            a = all_func(True)

    else:
        copyname = 'testReport/paas_test_api_ressult.html'
        try:
            a = requests.get('http://127.0.0.1:8090/checkedapi/', params={'env': ''}).json()
        except:
            a = all_func()
    for case in a:
        testsuits.addTest(
            unittest.defaultTestLoader.discover(path, pattern=case + '_test.py', top_level_dir='testCase'))
    result = BeautifulReport(testsuits)
    result.report(filename=report_name, description="API接口", log_path='testReport')
    shutil.copy('testReport/%s.html' % report_name, copyname)

    result_list = [item for item in result.result_list if item[4] != '成功']

    from PIL import Image, ImageDraw, ImageFont
    if result_list:

        length, weight_unit = 1000, 20
        back_img = Image.new(mode='RGB', size=(length, weight_unit * len(result_list)),
                             color=(255, 255, 255))
        draw_img = ImageDraw.ImageDraw(back_img)
        font = ImageFont.truetype('arial.ttf', size=weight_unit,encoding='gbk')

        num = 0
        for item in result_list:
            draw_img.text((0, weight_unit * num), item[0]+':'+item[1], font=font, fill='red')
            num += 1
            # draw_img.text((0, weight_unit * num), item[5][-1], font=font, fill='black')
            # num += 1
            # draw_img.text((0, weight_unit * num), '-'*10+'分割线'+'-'*10, font=font, fill='black')
            # num += 1
        back_img.save('testReport/error.jpg')
    else:
        back_img = Image.new(mode='RGB', size=(200,50),
                             color=(255, 255, 255))
        draw_img = ImageDraw.ImageDraw(back_img)
        font = ImageFont.truetype('simkai.ttf', size=50)
        draw_img.text((0, 0), '全部通过', font=font, fill='green')
        back_img.save('testReport/error.jpg')



    # try:
    #     # 对测试结果入库,本期对总执行数用例（非脚本数）和错误数量入库
    #     failure_count, error_count, success_count = result.failure_count, result.error_count, result.success_count
    #     # 调用接口入库
    #
    #     requests.post('http://127.0.0.1:8090/oms/autoresult',
    #                   data={"failure_count": failure_count, "error_count": error_count, "success_count": success_count})
    #
    #     # 对错误脚本入库
    #     error_list = [[item[0], item[1]] for item in result.result_list if item[4] == "失败"]
    #     requests.post('http://127.0.0.1:8090/oms/apiresult', data=json.dumps({"error_list": error_list}))
    # except:
    #     '''
    #     暂不实现
    #     '''
    #
    # # 全部做容错处理，django服务可能不稳定，在无法进行访问时，直接操作数据库
    # '''
    # http://127.0.0.1:8090/oms/checkedapi
    # http://127.0.0.1:8090/oms/autoresult
    # http://127.0.0.1:8090/oms/apiresult
    #
    # '''


if __name__ == "__main__":
    import os

    os.remove('testReport/error.jpg') if os.path.exists('testReport/error.jpg') else None

    run_test()

