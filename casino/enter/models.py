from django.db import models


class User(models.Model):
    login = models.CharField(max_length=20)
    gmail = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

