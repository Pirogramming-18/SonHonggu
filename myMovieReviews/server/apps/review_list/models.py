# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.config.settings")

# import django
# django.setup()

from django.db import models

# Create your models here.
# DB와 연결되는 파이썬 클래스를 models라고 한다

class Movie(models.Model):
    title = models.CharField(max_length=64)
    director = models.CharField(max_length=32)
    release_year = models.IntegerField()
    main_actor = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    score = models.FloatField()
    running_time = models.IntegerField()
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)