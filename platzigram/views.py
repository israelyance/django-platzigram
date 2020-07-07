'''Platzigram Views'''

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    '''Return a greeting'''
    return HttpResponse('0h, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))


def sort_integers(request):
    '''Return a JSON response with sorted integers'''
    # import pdb; pdb.set_trace()
    numbers = [int(x) for x in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json')


def say_hi(request, name, age):
    '''Return a greeting.'''
    if age < 12:
        message = 'Sorry {}. You are not allowed here'.format(name)
    else:
        message = 'Hello {}. Welcome to Platzigram'. format(name)
    return HttpResponse(message)