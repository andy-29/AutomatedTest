import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Face_Latest_Analyze_Result(unittest.TestCase):
    '''
    获取最新的人脸分析档案
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        cls.token = face_token_get(file=None)
    @data(*(get_values(func, "test_face_latest_analyze_result")))
    @require_login
    def test_face_latest_analyze_result(self,value):
        self._testMethodDoc = "--"
        '''
        获取最新的人脸分析档案
        '''
        # 循环检测
        num = 0
        while num < 5:
            time.sleep(6)
            r = gmhttp.get(self.url)
            self.assertEqual(200, r.status_code)
            r = r.json()
            if r.get('error') != 0:
                num += 1
                continue
            break
        self.assertEqual(r.get("error"), 0)
        self.assertNotEqual(5, num, msg='30秒内没有获取面部分析报告！')
        self.assertIn('data', r.keys())
        self.assertIn('last_modified', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('last_modified'), str)
        self.assertIn('simulated_image_url', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('simulated_image_url'), (type(None), str))
        self.assertIn('image_url', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('image_url'), str)
        self.assertIn('user_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('user_id'), int)
        self.assertIn('token', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('token'), str)
        self.assertIn('face_analyzed', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('face_analyzed'), dict)
        self.assertIn('eyebrow', r.get('data').get('face_analyzed').keys())
        self.assertIsInstance(r.get('data').get('face_analyzed').get('eyebrow'), dict)
        self.assertIn('contour', r.get('data').get('face_analyzed').keys())
        self.assertIsInstance(r.get('data').get('face_analyzed').get('contour'), dict)
        self.assertIn('nose', r.get('data').get('face_analyzed').keys())
        self.assertIsInstance(r.get('data').get('face_analyzed').get('nose'), dict)
        self.assertIn('eye', r.get('data').get('face_analyzed').keys())
        self.assertIsInstance(r.get('data').get('face_analyzed').get('eye'), dict)
        self.assertIn('chin', r.get('data').get('face_analyzed').keys())
        self.assertIsInstance(r.get('data').get('face_analyzed').get('chin'), dict)
        self.assertIn('lip', r.get('data').get('face_analyzed').keys())
        self.assertIsInstance(r.get('data').get('face_analyzed').get('lip'), dict)
        self.assertIn('simulated_text', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('simulated_text'), (type(None), str))
        self.assertIn('tag_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('tag_id'), int)
        self.assertIn('created_time', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('created_time'), str)
        self.assertIn('eyelid_simulated', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('eyelid_simulated'), bool)
        self.assertIn('landmark', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('landmark'), dict)
        self.assertIn('right_eye_lower_right_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_lower_right_quarter'), dict)
        self.assertIn('contour_right2', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right2'), dict)
        self.assertIn('left_eye_lower_right_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_lower_right_quarter'), dict)
        self.assertIn('right_eye_center', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_center'), dict)
        self.assertIn('contour_right3', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right3'), dict)
        self.assertIn('left_eyebrow_upper_right_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eyebrow_upper_right_quarter'), dict)
        self.assertIn('left_eyebrow_left_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eyebrow_left_corner'), dict)
        self.assertIn('right_eyebrow_upper_right_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eyebrow_upper_right_quarter'), dict)
        self.assertIn('contour_right4', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right4'), dict)
        self.assertIn('left_eye_upper_left_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_upper_left_quarter'), dict)
        self.assertIn('right_eyebrow_left_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eyebrow_left_corner'), dict)
        self.assertIn('contour_right1', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right1'), dict)
        self.assertIn('contour_left2', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left2'), dict)
        self.assertIn('right_eyebrow_lower_right_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eyebrow_lower_right_quarter'), dict)
        self.assertIn('mouth_upper_lip_left_contour3', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_upper_lip_left_contour3'), dict)
        self.assertIn('right_eyebrow_lower_left_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eyebrow_lower_left_quarter'), dict)
        self.assertIn('right_eye_lower_left_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_lower_left_quarter'), dict)
        self.assertIn('right_eyebrow_right_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eyebrow_right_corner'), dict)
        self.assertIn('left_eye_left_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_left_corner'), dict)
        self.assertIn('right_eyebrow_lower_middle', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eyebrow_lower_middle'), dict)
        self.assertIn('left_eye_pupil', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_pupil'), dict)
        self.assertIn('mouth_lower_lip_left_contour2', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_lower_lip_left_contour2'), dict)
        self.assertIn('left_eyebrow_lower_right_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eyebrow_lower_right_quarter'), dict)
        self.assertIn('mouth_lower_lip_bottom', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_lower_lip_bottom'), dict)
        self.assertIn('contour_left3', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left3'), dict)
        self.assertIn('mouth_left_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_left_corner'), dict)
        self.assertIn('contour_left6', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left6'), dict)
        self.assertIn('contour_left7', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left7'), dict)
        self.assertIn('contour_left5', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left5'), dict)
        self.assertIn('contour_left4', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left4'), dict)
        self.assertIn('left_eye_bottom', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_bottom'), dict)
        self.assertIn('right_eye_pupil', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_pupil'), dict)
        self.assertIn('contour_chin', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_chin'), dict)
        self.assertIn('contour_left9', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left9'), dict)
        self.assertIn('mouth_upper_lip_left_contour1', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_upper_lip_left_contour1'), dict)
        self.assertIn('right_eye_right_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_right_corner'), dict)
        self.assertIn('left_eyebrow_lower_left_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eyebrow_lower_left_quarter'), dict)
        self.assertIn('nose_contour_left2', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_contour_left2'), dict)
        self.assertIn('mouth_upper_lip_top', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_upper_lip_top'), dict)
        self.assertIn('mouth_lower_lip_left_contour1', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_lower_lip_left_contour1'), dict)
        self.assertIn('right_eye_upper_right_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_upper_right_quarter'), dict)
        self.assertIn('right_eyebrow_upper_middle', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eyebrow_upper_middle'), dict)
        self.assertIn('mouth_lower_lip_right_contour3', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_lower_lip_right_contour3'), dict)
        self.assertIn('contour_right7', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right7'), dict)
        self.assertIn('right_eye_bottom', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_bottom'), dict)
        self.assertIn('left_eye_right_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_right_corner'), dict)
        self.assertIn('contour_right6', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right6'), dict)
        self.assertIn('right_eye_left_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_left_corner'), dict)
        self.assertIn('nose_contour_left3', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_contour_left3'), dict)
        self.assertIn('contour_left1', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left1'), dict)
        self.assertIn('mouth_lower_lip_right_contour2', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_lower_lip_right_contour2'), dict)
        self.assertIn('mouth_upper_lip_right_contour2', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_upper_lip_right_contour2'), dict)
        self.assertIn('right_eye_top', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_top'), dict)
        self.assertIn('nose_contour_lower_middle', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_contour_lower_middle'), dict)
        self.assertIn('mouth_upper_lip_left_contour2', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_upper_lip_left_contour2'), dict)
        self.assertIn('contour_right5', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right5'), dict)
        self.assertIn('left_eyebrow_upper_middle', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eyebrow_upper_middle'), dict)
        self.assertIn('nose_tip', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_tip'), dict)
        self.assertIn('contour_left8', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_left8'), dict)
        self.assertIn('mouth_upper_lip_right_contour3', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_upper_lip_right_contour3'), dict)
        self.assertIn('mouth_upper_lip_bottom', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_upper_lip_bottom'), dict)
        self.assertIn('nose_left', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_left'), dict)
        self.assertIn('left_eye_upper_right_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_upper_right_quarter'), dict)
        self.assertIn('mouth_lower_lip_top', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_lower_lip_top'), dict)
        self.assertIn('nose_contour_right2', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_contour_right2'), dict)
        self.assertIn('mouth_lower_lip_right_contour1', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_lower_lip_right_contour1'), dict)
        self.assertIn('nose_contour_right1', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_contour_right1'), dict)
        self.assertIn('left_eyebrow_upper_left_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eyebrow_upper_left_quarter'), dict)
        self.assertIn('nose_contour_right3', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_contour_right3'), dict)
        self.assertIn('left_eye_lower_left_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_lower_left_quarter'), dict)
        self.assertIn('left_eyebrow_right_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eyebrow_right_corner'), dict)
        self.assertIn('left_eye_center', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_center'), dict)
        self.assertIn('nose_right', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_right'), dict)
        self.assertIn('left_eye_top', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eye_top'), dict)
        self.assertIn('contour_right9', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right9'), dict)
        self.assertIn('mouth_right_corner', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_right_corner'), dict)
        self.assertIn('nose_contour_left1', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('nose_contour_left1'), dict)
        self.assertIn('left_eyebrow_lower_middle', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('left_eyebrow_lower_middle'), dict)
        self.assertIn('right_eyebrow_upper_left_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eyebrow_upper_left_quarter'), dict)
        self.assertIn('right_eye_upper_left_quarter', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('right_eye_upper_left_quarter'), dict)
        self.assertIn('mouth_upper_lip_right_contour1', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_upper_lip_right_contour1'), dict)
        self.assertIn('contour_right8', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('contour_right8'), dict)
        self.assertIn('mouth_lower_lip_left_contour3', r.get('data').get('landmark').keys())
        self.assertIsInstance(r.get('data').get('landmark').get('mouth_lower_lip_left_contour3'), dict)
        self.assertIn('simulated_type', r.get('data').keys())
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Face_Latest_Analyze_Result.run()