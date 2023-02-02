import os
import requests
import urllib3
urllib3.disable_warnings()
from tqdm import tqdm
import time
from numpy.random import uniform
import cv2
import numpy
from PIL import Image


class Set_Params:
    Set_Cookies = {
    'BA_HECTOR': '8h24a024042g05alup1h3g0aq0q',
    'BAIDUID': '104BD58A7C408DABABCAC9E0A1B184B4:FG=1',
    'BAIDUID_BFESS': '104BD58A7C408DABABCAC9E0A1B184B4:FG=1',
    'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
    'BDRCVFR[-pGxjrCMryR]': 'mk3SLVN4HKm',
    'BDRCVFR[dG2JNJb_ajR]': 'mk3SLVN4HKm',
    'BDSFRCVID': '8--OJexroG0xMovDbuOS5T78igKKHJQTDYLtOwXPsp3LGJLVgaSTEG0PtjcEHMA-2ZlgogKK02OTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
    'BDSFRCVID_BFESS': '8--OJexroG0xMovDbuOS5T78igKKHJQTDYLtOwXPsp3LGJLVgaSTEG0PtjcEHMA-2ZlgogKK02OTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
    'BDqhfp': '%E7%8B%97%E7%8B%97%26%26NaN-1undefined%26%2618880%26%2621',
    'BIDUPSID': '06338E0BE23C6ADB52165ACEB972355B',
    'H_BDCLCKID_SF': 'tJPqoKtbtDI3fP36qR3KhPt8Kpby2D62aKDs2nopBhcqEIL4QTQM5p5yQ2c7LUvtynT2KJnz3Po8MUbSj4QoDjFjXJ7RJRJbK6vwKJ5s5h5nhMJSb67JDMP0-4F8exry523ioIovQpn0MhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0D6bBjHujtT_s2TTKLPK8fCnBDP59MDTjhPrMypomWMT-0bFH_-5L-l5js56SbU5hW5LSQxQ3QhLDQNn7_JjOX-0bVIj6Wl_-etP3yarQhxQxtNRdXInjtpvhHR38MpbobUPUDa59LUvEJgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLtD8bMC-RDjt35n-Wqxobbtof-KOhLTrJaDkWsx7Oy4oTj6DD5lrG0P6RHmb8ht59JROPSU7mhqb_3MvB-fnEbf7r-2TP_R6GBPQtqMbIQft20-DIeMtjBMJaJRCqWR7jWhk2hl72ybCMQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8EjHCet5DJJn4j_Dv5b-0aKRcY-tT5M-Lf5eT22-usy6Qd2hcH0KLKDh6gb4PhQKuZ5qutLTb4QTbqWKJcKfb1MRjvMPnF-tKZDb-JXtr92nuDal5TtUthSDnTDMRhXfIL04nyKMnitnr9-pnLJpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuj6tWj6j0DNRabK6aKC5bL6rJabC3b5CzXU6q2bDeQN3OW4Rq3Irt2M8aQI0WjJ3oyU7k0q0vWtvJWbbvLT7johRTWqR4enjb3MonDh83Mxb4BUrCHRrzWn3O5hvvhKoO3MA-yUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCqVIKa3f',
    'H_BDCLCKID_SF_BFESS': 'tJPqoKtbtDI3fP36qR3KhPt8Kpby2D62aKDs2nopBhcqEIL4QTQM5p5yQ2c7LUvtynT2KJnz3Po8MUbSj4QoDjFjXJ7RJRJbK6vwKJ5s5h5nhMJSb67JDMP0-4F8exry523ioIovQpn0MhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0D6bBjHujtT_s2TTKLPK8fCnBDP59MDTjhPrMypomWMT-0bFH_-5L-l5js56SbU5hW5LSQxQ3QhLDQNn7_JjOX-0bVIj6Wl_-etP3yarQhxQxtNRdXInjtpvhHR38MpbobUPUDa59LUvEJgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLtD8bMC-RDjt35n-Wqxobbtof-KOhLTrJaDkWsx7Oy4oTj6DD5lrG0P6RHmb8ht59JROPSU7mhqb_3MvB-fnEbf7r-2TP_R6GBPQtqMbIQft20-DIeMtjBMJaJRCqWR7jWhk2hl72ybCMQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8EjHCet5DJJn4j_Dv5b-0aKRcY-tT5M-Lf5eT22-usy6Qd2hcH0KLKDh6gb4PhQKuZ5qutLTb4QTbqWKJcKfb1MRjvMPnF-tKZDb-JXtr92nuDal5TtUthSDnTDMRhXfIL04nyKMnitnr9-pnLJpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuj6tWj6j0DNRabK6aKC5bL6rJabC3b5CzXU6q2bDeQN3OW4Rq3Irt2M8aQI0WjJ3oyU7k0q0vWtvJWbbvLT7johRTWqR4enjb3MonDh83Mxb4BUrCHRrzWn3O5hvvhKoO3MA-yUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCqVIKa3f',
    'H_PS_PSSID': '35836_35105_31254_36024_36005_34584_36142_36120_36032_35993_35984_35319_26350_35723_22160_36061',
    'PSINO': '2',
    'PSTM': '1646905430',
    'ab_sr': '1.0.1_Y2YxZDkwMWZkMmY2MzA4MGU0OTNhMzVlNTcwMmM2MWE4YWU4OTc1ZjZmZDM2N2RjYmVkMzFiY2NjNWM4Nzk4NzBlZTliYWU0ZTAyODkzNDA3YzNiMTVjMTllMzQ0MGJlZjAwYzk5MDdjNWM0MzJmMDdhOWNhYTZhMjIwODc5MDMxN2QyMmE1YTFmN2QyY2M1M2VmZDkzMjMyOThiYmNhZA==',
    'cleanHistoryStatus': '0',
    'delPer': '0',
    'indexPageSugList': '%5B%22%E7%8B%97%E7%8B%97%22%5D',
    }

    Set_Headers = {
    'Referer': 'https://image.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'text/plain, */*;q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9, en;q=0.8, en-GB;q=0.7, en-US;q=0.6',
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    }


class Pic_Craw(Set_Params):
    def __init__(self, Class_List, Download_NUM):
        self.Attr_Class_List = Class_List
        self.Attr_Download_NUM = Download_NUM

    def Crawer(self, Cookies, Headers):
        for Keyword in self.Attr_Class_List:
            if not os.path.exists('DataSet'):
                os.makedirs('DataSet')
                print('新建DataSet文件夹')
            if os.path.exists('DataSet/' + Keyword):
                print('文件夹 DataSet/{}已存在，之后直接将爬取到的图片保存至该文件夹中'.format(Keyword))
            else:
                os.makedirs('DataSet/{}'.format(Keyword))
                print('新建文件夹：DataSet/{}'.format(Keyword))
            COUNT = 1
            with tqdm(total = self.Attr_Download_NUM, position = 0, leave = True) as ProgressBar:
                NUM = 1
                Break_Flag = False
                while not Break_Flag:
                    PAGE = 30 * COUNT
                    Params = (
                        ('tn', 'resultjson_com'),
                        ('logid', '12508239107856075440'),
                        ('ipn', 'rj'),
                        ('ct', '201326592'),
                        ('is', ''),
                        ('fp', 'result'),
                        ('fr', ''),
                        ('word', f'{Keyword}'),
                        ('queryWord', f'{Keyword}'),
                        ('cl', '2'),
                        ('lm', '-1'),
                        ('ie', 'utf-8'),
                        ('oe', 'utf-8'),
                        ('adpicid', ''),
                        ('st', '-1'),
                        ('z', ''),
                        ('ic', ''),
                        ('hd', ''),
                        ('latest', ''),
                        ('copyright', ''),
                        ('s', ''),
                        ('se', ''),
                        ('tab', ''),
                        ('width', ''),
                        ('height', ''),
                        ('face', '0'),
                        ('istype', '2'),
                        ('qc', ''),
                        ('nc', '1'),
                        ('expermode', ''),
                        ('nojc', ''),
                        ('isAsync', ''),
                        ('pn', f'{PAGE}'),
                        ('rn', '30'),
                        ('gsm', '1e'),
                        ('1647838001666', ''),
                    )
                    Response = requests.get('https://image.baidu.com/search/acjson', headers = Headers, params = Params, cookies = Cookies)
                    if Response.status_code == 200:
                        try:
                            JSON_Data = Response.json().get('data')
                            if JSON_Data:
                                for x in JSON_Data:
                                    Type = x.get('type')
                                    if Type not in ['gif']:
                                        IMG = x.get('thumbURL') # 如果改为"objURL"（高清原图）很快会被反爬，慎用！
                                        PageTitle = x.get('fromPageTitleEnc')
                                        try:
                                            Response = requests.get(url = IMG, verify = False)
                                            time.sleep(uniform(1.2, 2.1))
                                            File_Save_Path = f'DataSet/{Keyword}/{NUM}.{Type}' # 若想保留图片原标题，在.{Type}前加上{PageTitle}即可
                                            with open(File_Save_Path, 'wb') as File:
                                                File.write(Response.content)
                                                File.flush()
                                                NUM += 1
                                                ProgressBar.update(1)
                                            if NUM > self.Attr_Download_NUM:
                                                if not Break_Flag:
                                                    Break_Flag = True
                                                print(f'{NUM - 1}张图像爬取完毕')
                                                break
                                        except Exception:
                                            pass
                        except:
                            pass
                    else:
                        break
                    COUNT += 1