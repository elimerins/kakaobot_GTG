from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from kakaobotapp import lecturealgo
from kakaobotapp import lecture

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

gachonliberalart_college=[]
ruddud_eo=['경영학과','경영학과(글로벌경영학트랙)','금융수학과']
tkrhk_eo=['행정학과','미디어커뮤니케이션학과','관광경영학과','글로벌경제학과','헬스케어경영학과',
          '응용통계학과','유아교육학과']
dlsanse_eo=['한국어문학과','영미어문학과','동양어문학과','유럽어문학과']
qjqrhk_eo=['법학과','경찰안보학과']
rhdrhk_eo=['도시계획학과','조경학과','실내건축학과','건축학과','건축공학과','전기공학과','설비·소방공학과',
           '화공생명공학과','환경에너지공학과','기계공학과','토목환경공학','산업경영공학']
qksk_eo=['바이노나노학과','나노화학과','나노물리학과','생명과학과','식품생물공학과','식품영양학과']
IT_eo=['소프트웨어학과','컴퓨터공학과','전자공학과','에너지IT학과']
gksdml_eo=['한의예과']
dP_eo=['회화','조소','시각디자인','산업디자인','패션디자인','성악','기악','작곡',
       '체육','태권도','연기예술학']
dml_eo=['의예과','의학과']
dir_eo=['약학과']
rksgh_eo=['간호학과']
qhrjsrhkgkr_eo=['치위생학과','응급구조학과','방사선학과','물리치료학과','의용생체공학과',
                '운동재활복지학과']
# Create your views here.
credit_rangelist=['9 ~ 12','13 ~ 15','16 ~ 18']
grade_rangelist=['1','2','3','4','5']
major=''
usergrade=''
def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['안녕하세요!'
                    ]
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    global major
    global usergrade

    datarestart='처음부터'
    if datacontent == '처음부터'or datacontent == '안녕하세요!':
        choice_college = "단과대학을 선택해주세요"
        major=''
        usergrade=0
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
                    '한의대학',
                    '예술대학',
                    '약학대학',
                    '간호대학',
                    '의과대학',
                    '보건과학대학',
                    datarestart]#마지막은 항상 처음부터로 시작
            }
            #단과대학 for range(array)형식으로 넣을것

        })
    elif datacontent=='경영대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [ruddud_eo[0],
                            ruddud_eo[1],
                            ruddud_eo[2],
                            datarestart]
            }

        })
    elif datacontent=='사회과학대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [tkrhk_eo[0],
                            tkrhk_eo[1],
                            tkrhk_eo[2],
                            tkrhk_eo[3],
                            tkrhk_eo[4],
                            tkrhk_eo[5],
                            tkrhk_eo[6],
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
    elif datacontent == '공과대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [rhdrhk_eo[0],
                            rhdrhk_eo[1],
                            rhdrhk_eo[2],
                            rhdrhk_eo[3],
                            rhdrhk_eo[4],
                            rhdrhk_eo[5],
                            rhdrhk_eo[6],
                            rhdrhk_eo[7],
                            rhdrhk_eo[8],
                            rhdrhk_eo[9],
                            rhdrhk_eo[10],
                            rhdrhk_eo[11],
                            rhdrhk_eo[12],
                            datarestart]
            }

        })
    elif datacontent == '바이노나오대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [qksk_eo[0],
                            qksk_eo[1],
                            qksk_eo[2],
                            qksk_eo[3],
                            qksk_eo[4],
                            qksk_eo[5],
                            datarestart]
            }

        })
    elif datacontent == 'IT대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [IT_eo[0],
                            IT_eo[1],
                            IT_eo[2],
                            IT_eo[3],
                            datarestart]
            }

        })
    elif datacontent == '한의과대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [gksdml_eo[0],
                            datarestart]
            }

        })
    elif datacontent == '예술대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [dP_eo[0],
                            dP_eo[1],
                            dP_eo[2],
                            dP_eo[3],
                            dP_eo[4],
                            dP_eo[5],
                            dP_eo[6],
                            dP_eo[7],
                            dP_eo[8],
                            dP_eo[9],
                            dP_eo[10],
                            datarestart]
            }

        })
    elif datacontent == '약학대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [dir_eo[0],
                            datarestart]
            }

        })
    elif datacontent == '한의대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [gksdml_eo[0],
                            datarestart]
            }

        })
    elif datacontent == '의과대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [dml_eo[0],
                            dml_eo[1],
                            datarestart]
            }

        })
    elif datacontent == '간호대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [rksgh_eo[0],
                            datarestart]
            }

        })
    elif datacontent == '보건과학대학':
        tomorrow = "학과를 선택해주세요"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': [qhrjsrhkgkr_eo[0],
                            qhrjsrhkgkr_eo[1],
                            qhrjsrhkgkr_eo[2],
                            qhrjsrhkgkr_eo[3],
                            qhrjsrhkgkr_eo[4],
                            qhrjsrhkgkr_eo[5],
                            datarestart]
            }

        })
    elif any(datacontent in s for s in ruddud_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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

    elif any(datacontent in s for s in tkrhk_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in dlsanse_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in qjqrhk_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in rhdrhk_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
                            '5',
                            datarestart
                            ]
            }

        })
    elif any(datacontent in s for s in qksk_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in IT_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in gksdml_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in dP_eo):#예대
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in dir_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in rksgh_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
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
    elif any(datacontent in s for s in qhrjsrhkgkr_eo):
        grade = "학년을 선택해주세요"
        major=datacontent
        return JsonResponse({
            'message': {
                'text':
                    grade
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

    elif any(datacontent in s for s in grade_rangelist):
        credit_range = "학점 범위를 선택해주세요"
        usergrade = datacontent
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

    elif datacontent==credit_rangelist[0]:
        print(major+' '+usergrade+' '+datacontent)
        if(major=='시각디자인' or major=='산업디자인'):
            major='미술·디자인학부(디자인)'
        elif(major=='미디어커뮤니케이션학과'):
            major='신문방송학과'
        elif(major=='금융수학과'):
            major='수학정보학과'
        elif(major=='글로벌경제학과'):
            major='무역학과'

        list=lecturealgo.generator(9,12,major,usergrade)
        return JsonResponse({
            'message':{
                'text':major+'\n'+usergrade+'\n'+datacontent+'\n'+str(list)
            },
            'keyboard':{
                'type':'buttons',
                'buttons':[
                    datarestart
                ]
            }
        })

    elif datacontent==credit_rangelist[1]:
        print(major + ' ' + usergrade + ' ' + datacontent)
        if (major == '시각디자인' or major == '산업디자인'):
            major = '미술·디자인학부(디자인)'
        elif (major == '미디어커뮤니케이션학과'):
            major = '신문방송학과'
        elif (major == '금융수학과'):
            major = '수학정보학과'
        elif (major == '글로벌경제학과'):
            major = '무역학과'
        list=lecturealgo.generator(13,15,major,usergrade)
        return JsonResponse({
            'message':{
                'text':major+'\n'+usergrade+'\n'+datacontent+'\n'+str(list)
            },
            'keyboard':{
                'type':'buttons',
                'buttons':[
                    datarestart
                ]
            }
        })
    elif datacontent==credit_rangelist[2]:
        print(major + ' ' + usergrade + ' ' + datacontent)
        if (major == '시각디자인' or major == '산업디자인'):
            major = '미술·디자인학부(디자인)'
        elif (major == '미디어커뮤니케이션학과'):
            major = '신문방송학과'
        elif (major == '금융수학과'):
            major = '수학정보학과'
        elif (major == '글로벌경제학과'):
            major = '무역학과'
        list=lecturealgo.generator(16,18,major,usergrade)

        return JsonResponse({
            'message':{
                'text':major+'\n'+usergrade+'\n'+'\n'+datacontent+'\n'+str(list)
            },
            'keyboard':{
                'type':'buttons',
                'buttons':[
                    datarestart
                ]
            }
        })

