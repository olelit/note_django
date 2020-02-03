from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
