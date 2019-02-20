'''
本模块提供各种id的获取
'''
from common.get_config import g
from common.getcookie import require_login, gmhttp
import os, time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@require_login
def question_id_get():
    r = gmhttp.get(url=g.host + g.get_info('api_info', 'question_index_v2')).json()
    question_id = r['data']['topics'][0]['question_id']
    zone_id = r['data']['recommend_zones'][0]['zone_id']
    return question_id, zone_id


@require_login
def answer_id_get():
    post_data = {'question_id': str(question_id_get()), 'content': '[{"content":"美分美分美分","type":0}]'}
    gmhttp.post(url=g.host + '/api/question/create_answer', data=post_data)
    r = gmhttp.get(url=g.host + '/api/user/my_answer').json()
    return r['data'][0]['answer_id']


@require_login
def customer_srv_id_get():
    r = gmhttp.get(url=g.host + '/api/customer_srv/is_direct_talk').json()
    entry_id = r['data']['entry_id']
    user_key = r['data']['user_key']
    return entry_id, user_key


# 获取美购（含机构和医生）   ---使用固定的测试美购等
# def service_id_get():
#     url = g.host + g.get_info('api_info', 'service_home_v3')
#     r = gmhttp.get(url).json()
#     for item in r.get('data').get('services'):
#         service_id = item.get('service_id')
#         if service_id:
#             # 获取医生id和医院id
#             gmhttp.params.update({"service_id": service_id})
#             url = g.host + g.get_info('api_info', 'service_detail_v1')
#             r = gmhttp.get(url).json()
#             gmhttp.reset()
#             doctor_id = r.get('data').get('service_hospital').get('doctor_id')
#             hospital_id = r.get('data').get('service_hospital').get('hospital_id')
#             sku_id = r.get('data').get('normal_sku_list')[0].get('service_item_id')
#             if all((doctor_id, hospital_id, sku_id)):
#                 return service_id, hospital_id, doctor_id, sku_id


def service_id_get():
        service_id = 5450353
        # 获取医生id和医院id
        gmhttp.params.update({"service_id": service_id})
        url = g.host + g.get_info('api_info', 'service_detail_v1')
        r = gmhttp.get(url).json()
        gmhttp.reset()
        doctor_id = r.get('data').get('service_hospital').get('doctor_id')
        hospital_id = r.get('data').get('service_hospital').get('hospital_id')
        sku_id = r.get('data').get('normal_sku_list')[0].get('service_item_id')

        return service_id, hospital_id, doctor_id, sku_id


@require_login
def diary_id_get():
    api_setup_1 = g.get_info('api_info', 'user_my_diary_v2')
    url = g.host + api_setup_1
    r = gmhttp.get(url).json()
    diary_id = r['data']['diaries'][0]['id'] if r['data']['diaries'] else False
    # =============================================
    if not diary_id:
        diary_id = create_diary()
    return diary_id



def diary_id_others_get():
    url = g.host + g.get_info('api_info', 'index_v6')
    r = gmhttp.get(url).json()
    diary_id = r.get('data').get('features')[0].get('id')
    return diary_id


@require_login
def create_diary():
    tag_id1 = g.get_info('env_info', 'tag_id1')
    api_step1 = g.get_info('api_info', 'diary_additional_info_v2')
    url = g.host + api_step1
    r = gmhttp.post(url, data={
        'tag_ids': '[{}]'.format(tag_id1),
        'operation_timestamp': int(time.time()),
        'cover': '',
        'images': []
    }).json()
    diary_id = r.get('data').get('id')
    return diary_id


@require_login
def file_name_get():
    # 上传图片,图片放在conmmon下
    url = g.host + '/files/upload/'
    with open(os.path.join(BASE_DIR, 'common', 'test.jpg'), 'rb') as f:
        info = f.read()
    files = {"file": ('test.jpg', info, 'image/jpg')}
    r = gmhttp.post(url, files=files).json()
    file_name = r.get('data').get('file')
    return file_name


@require_login
def draft_id_get():
    # 创建草稿
    add_draft = g.get_info('api_info', 'draft_create')
    url = g.host + add_draft
    tag_id1 = g.get_info('env_info', 'tag_id1')
    r = gmhttp.post(url, data={
        'draft_type': 0,  # 类型为1需要后期添加
        'content': '草稿测试',
        'cover': '',
        'diary_id': diary_id_get(),
        'images': [],
        'tag_ids': '[' + tag_id1 + ']'
    }).json()

    draft_id = r.get('data').get('draft_id')
    return draft_id


def face_file_name_get():
    url = g.host + '/files/upload/face'
    with open(os.path.join(BASE_DIR, 'common', 'test.jpg'), 'rb') as f:
        info = f.read()
    files = {"file": ('test.jpg', info, 'image/jpg')}
    r = gmhttp.post(url, files=files).json()
    file_name = r.get('data').get('file')
    return file_name


def face_token_get(file):
    url = g.host + g.get_info('api_info', 'face_analyze')
    if not file:
        file = face_file_name_get()
    r = gmhttp.post(url, data={"filename": file}).json()
    token = r.get('data').get('token')
    return token


def live_topic_id_get():
    uri = g.get_info('api_info', 'live_list')
    url = g.host + uri
    r = gmhttp.get(url).json()
    topic_list = list(map(lambda x: x.get('topic_id'), filter(lambda x: x.get('status') == 0, r.get('data'))))[0]
    return topic_list


@require_login
def order_settlement_id_get():
    # 订单和付款单
    uri = g.get_info('api_info', 'orders_my_v2')
    url = g.host + uri
    r = gmhttp.get(url).json()
    order_id = settlement_id = None
    for item in r['data']['orders']:
        order_id = item['order']['order_id']
        settlement_id = item['order']['settlement_id']
        break
    return order_id, settlement_id


# def tag_id_get():
#     uri = g.get_info('api_info', 'tag_list')
#     url = g.host + uri
#     r = gmhttp.get(url).json()
#     tag_id =


def reason_id_get():
    url = g.host + g.get_info('api_info', 'report_reason')
    r = gmhttp.get(url).json()
    reason_id = r.get('data')[0].get('reason_id')
    return reason_id


@require_login
def shopcart_info_get():
    url = g.host + g.get_info('api_info', 'shopcart_list_v2')
    gmhttp.params.update({'count_only': 0})
    r = gmhttp.get(url).json()

    if not r['data']['cart']:
        *_,service_item_id = service_id_get()
        post_data = {'number': '1', 'service_item_id': service_item_id}
        gmhttp.post(url=g.host + g.get_info('api_info', 'shopcart_add_v1'), data=post_data).json()
        r = gmhttp.get(url).json()
    gmhttp.reset()
    service_item_id = r['data']['cart'][0]['services'][0]['service_item_id']
    myid = r['data']['cart'][0]['services'][0]['id']  # 获取购物车物品id
    service_id = r['data']['cart'][0]['services'][0]['service_id']
    transparent_key = r['data']['interesting'][0]['gm_url'].split('=')[2]
    return myid, service_item_id, service_id, transparent_key


@require_login
def uid_get():
    url = g.host + g.get_info('api_info', 'user_info')
    r = gmhttp.get(url).json()
    user_id = r.get('data').get('uid')
    return user_id


@require_login
def zone_my_get():
    r = gmhttp.get(url=g.host + g.get_info('api_info', 'zone_my')).json()
    if not r['data']['my_tags']:
        _, zone_id = question_id_get()
        post_data = {'tag_id': zone_id}
        gmhttp.post(url=g.host + g.get_info('api_info', 'zone_follow'), data=post_data).json()
    r = gmhttp.get(url=g.host + g.get_info('api_info', 'zone_my')).json()
    tag_name = r['data']['my_tags'][0]['name']
    tag_id = r['data']['my_tags'][0]['tag_id']
    return tag_id, tag_name


def settlement_id_get():
    data = {"service_item_id": "78123", "number": "1", "phone": "77777777777", "platform_coupon_id": "",
            "doctor_coupon_id": "", "use_point": "0", "is_doctor_see": "1", "insurance_info": "[]"}
    r = gmhttp.post(url=g.host + g.get_info('api_info', 'settlement_create_v1'), data=data).json()
    st_id = r.get('data').get('id')
    return st_id

@require_login
def maidan_id_get():
    *_, doctor_id, _ = service_id_get()
    data = {
        'tag_ids': "[0]",
        "payment": 0,
        "doctor_id": doctor_id
    }
    url = g.host + g.get_info('api_info','maidan_create')
    r = gmhttp.post(url=url, data=data).json()
    maidan_id = r.get('data').get('id')
    return maidan_id

@require_login
def sign_activity_id_get():
    url = g.host + g.get_info('api_info','sign_detail')
    r = gmhttp.get(url).json()
    activity_id = r.get('data').get('id')
    status = r.get('data').get('is_remind')
    sign_status = r.get('data').get('sign_status')
    total_days = r.get('data').get('total_days')

    return activity_id,status,sign_status,total_days


