from django.db import models
from extensions.utils import jalali_converter
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def jcreated(self):
        return jalali_converter(self.created)

    def __str__(self):
        return self.title
