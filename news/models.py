from django.db import models


class NewsTable(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=32)
    article = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
