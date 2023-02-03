from django.db import models


class tests(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()


class questions(models.Model):
    name = models.CharField(max_length=2000)
    type = models.CharField(max_length=100)
    order = models.IntegerField()


class answers(models.Model):
    answer = models.CharField(max_length=1000)
    correct = models.BooleanField()
    comments = models.TextField()
    order = models.IntegerField()
