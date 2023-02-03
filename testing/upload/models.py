from django.db import models


class tests(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()


class questions(models.Model):
    test_name = models.CharField(max_length=150)
    name = models.CharField(max_length=2000)
    type = models.CharField(max_length=100)
    order = models.IntegerField()


class answers(models.Model):
    questions_name = models.CharField(max_length=2000)
    answer = models.CharField(max_length=1000)
    correct = models.BooleanField()
    comments = models.TextField()
    order = models.IntegerField()
