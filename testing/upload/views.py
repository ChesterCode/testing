import questions as questions
from django.http import HttpResponse
from django.shortcuts import render
from .models import questions
def index(request):
    questions = questions.objects.all()
    res = "<h1>Список вопросов</h1>"
    for item in questions:
        res += f'<div>\n<p>{item.name}</p>\n</div\n<hr>'
    return HttpResponse(res)

    return HttpResponse("Страница загрузки")
