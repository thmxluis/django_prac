# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('Hola  la fecha del servidor es {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_ints(request):
    # Return a JSON response whith sorted integers.
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'estatus': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(request, name, age):
    # Returns Entrada condicionada
    if age < 12:
        message = 'Sorry {}, you are not allowed'.format(name)
    else:
        message = 'Hello {}, Welcome to platzigram'.format(name)

    return HttpResponse(message)
