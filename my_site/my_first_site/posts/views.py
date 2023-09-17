from django.shortcuts import render

from django.http import HttpResponse

POSTS = {'text': 'Сделал это сидя на паре йоу',
         'title': 'Это мой проект'
}

def index(request):
    return HttpResponse(f'Это я сделал, {POSTS}')