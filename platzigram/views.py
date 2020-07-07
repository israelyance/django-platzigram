'''Platzigram Views'''

# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    '''Return a greeting'''
    return HttpResponse('0h, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def hi(request):
    '''Hi'''
    # import pdb; pdb.set_trace()
    numbers = sorted([int(x) for x in request.GET['numbers'].split(',')])
    response = JsonResponse([numbers], safe=False)
    return response