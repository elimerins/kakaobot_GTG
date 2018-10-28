from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from kakaobotapp import lecturealgo
import copy
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='password',
                       db='gtg', charset='utf8')
curs = conn.cursor()
sql = "select * from mj"
curs.execute(sql)
rows = curs.fetchall()
maj_cd_list=[]
for index in rows:
    maj_cd_list.append(index[2])
college_list=['사회과학대학','경영대학','인문대학','법과대학','공과대학','바이오나노대학','IT대학',
              '예술대학','가천리버럴아츠칼리지','창조융합원','글로벌교양대학','생활과학대학','간호대학','의과대학','자연과학대학']
major=''
grade=0
gachonliberalart_college=[]
ruddud_eo=['경영학과','글로벌경영학과','금융수학']
tkrhk_eo=['행정학과','미디어커뮤니케이션학과','관광경영학과','글로벌경제학과','헬스케어경영학과','응용통계학과','유아교육학과']
dlsanse_eo=['한국어문학과','영미어문학과','동양어문학과','유럽어문학과']
qjqrhk_eo=['법학과','경찰안보학과']
rhdrhk_eo=['도시계획학과','조경학과','실내건축학과','건축학과','건축공학과','전기공학과','설비소방공학과',
           '화공생명공학과','환경에너지공학과','기계공학과','토목환경공학','산업경영공학','신소재공학과']
qksk_eo=['바이노나노학과','나노화학과','나노물리학과','생명과학과','식품생물공학과','식품영양학과']
IT_eo=['소프트웨어학과','컴퓨터공학과','전자공학과','에너지IT학과']
gksdml_eo=['한의예과']
dP_eo=['회화','조소','시각디자인','산업디자인','패션디자인','성악','기악','작곡','체육','태권도','연기예술학']
dml_eo=['의예과','의학과']
dir_eo=['약학과']
rksgh_eo=['간호학과']
qhrjsrhkgkr_eo=['치위생학과','응급구조학과','방사선학과','물리치료학과','의용생체공학과','운동재활복지학과']
# Create your views here.

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['사회과학대학',
                    '경영대학',
                    '인문대학',
                    '법과대학',
                    '공과대학',
                    '바이오나노대학',
                    'IT대학',
                    '예술대학',
                    '가천리버럴아츠칼리지',
                    '창조융합원',
                    '글로벌교양대학',
                    '생활과학대학',
                    '간호대학',
                    '의과대학',
                    '자연과학대학'
                    ]
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    datarestart='처음부터'
    if datacontent == '처음부터':
        choice_college = "단과대학을 선택해주세요"
        cpmajor=datacontent
        return JsonResponse({

            'message': {
                'text': choice_college
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['사회과학대학',
                    '경영대학',
                    '인문대학',
                    '법과대학',
                    '공과대학',
                    '바이오나노대학',
                    'IT대학',
                    '예술대학',
                    '가천리버럴아츠칼리지',
                    '창조융합원',
                    '글로벌교양대학',
                    '생활과학대학',
                    '간호대학',
                    '의과대학',
                    '자연과학대학',
                            datarestart]#마지막은 항상 처음부터로 시작
            }
            #단과대학 for range(array)형식으로 넣을것

        })
    elif any(datacontent in s for s in college_list):
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전자공학과',
                            '컴퓨터공학과',
                            datarestart]
            }

        })
    elif any(datacontent in s for s in college_list):
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['법학과',
                            '경찰안보학과',
                            datarestart]
            }

        })
    elif datacontent == '법과대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [qjqrhk_eo[0],
                            qjqrhk_eo[1],
                            datarestart]
            }

        })
    elif datacontent=="컴퓨터공학과":
        grade = "학년을 선택해주세요"
        return JsonResponse({
            'message': {
                'text': grade
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['1',
                            '2',
                            '3',
                            '4',
                            datarestart
                            ]
            }

        })
    elif datacontent=='2':
        credit_range="학점 범위를 선택해주세요"
        credit_rangelist=['9 ~ 12',
                     '13 ~ 15',
                     '16 ~ 18',]
        return JsonResponse({
            'message':{
                'text':credit_range
            },
            'keyboard':{
                'type':'buttons',
                'buttons': [
                    credit_rangelist[0],
                    credit_rangelist[1],
                    credit_rangelist[2],
                    datarestart
                ]

            }
        })
    elif datacontent=='9 ~ 12':
        waiting_message='잠시만 기다려주세요!'
        list=str(lecturealgo.generator(9,12,major,grade))
        return JsonResponse({
            'message':{
                'text':list
            },
            'keyboard':{
                'type':'buttons',
                'buttons':[
                    datarestart
                ]
            }
        })
    elif datacontent=='13 ~ 15':
        waiting_message='잠시만 기다려주세요!'
        list=str(lecturealgo.generator(13,15,major,grade))
        return JsonResponse({
            'message':{
                'text':list
            },
            'keyboard':{
                'type':'buttons',
                'buttons':[
                    datarestart
                ]
            }
        })
    elif datacontent=='16 ~ 18':
        waiting_message='잠시만 기다려주세요!'
        list=str(lecturealgo.generator(16,18,major,grade))
        return JsonResponse({
            'message':{
                'text':list
            },
            'keyboard':{
                'type':'buttons',
                'buttons':[
                    datarestart
                ]
            }
        })

