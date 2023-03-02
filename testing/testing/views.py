from django.shortcuts import render, redirect
from upload.models import questions
from upload.models import answers
from upload.models import tests

from django.db import connection


def index(request):
    upload = questions.objects.all()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) AS COUNT FROM upload_questions')
    count_value = cursor.fetchone()[0]
    return render(request, 'index.html', {'upload': upload, 'title': 'Список вопросов', 'count_value': count_value})
def delete(request):
    cursor = connection.cursor()
    cursor.execute('SELECT min(id) AS COUNT FROM upload_questions')
    min_value = cursor.fetchone()[0]
    delete = questions.objects.filter(id=min_value).delete()
    return redirect('home')