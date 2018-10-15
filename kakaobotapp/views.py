from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.
def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['사회과학대학',
                    '경영대학',
                    '법과대학',
                    '공과대학',
                    '예술대학',
                    'IT대학',
                    '생활과학대학'
                    ]
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    datarestart='처음부터'
    choice_department='학과를 선택해주세요'

    if datacontent == '처음부터':
        choice_college = "단과대학을 선택해주세요"

        return JsonResponse({

            'message': {
                'text': choice_college
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['경제학과',
                            '행정학과',
                            datarestart]#마지막은 항상 처음부터로 시작
            }
            #단과대학 for range(array)형식으로 넣을것

        })
    elif datacontent == 'IT대학':
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
    elif datacontent == 'IT대학':
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
    elif datacontent == '법과대학':
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
    elif datacontent=="전자공학과":
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
                            datarestart]
            }

        })
