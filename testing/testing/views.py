from django.shortcuts import render
from upload.models import questions
from upload.models import answers
from upload.models import tests

def index(request):
    upload = questions.objects.all()
    return render(request, 'index.html', {'upload': upload, 'title': 'Список вопросов'})