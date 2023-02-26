from django.http import HttpResponse
from django.shortcuts import render
from upload.models import questions
from upload.models import answers
from upload.models import tests

def index(request):
    upload = questions.objects.all()
    return render(request, 'upload/index.html', {'upload': upload, 'title': 'Список вопросов'})

def upload(request):
    return HttpResponse("Страница загрузки")
