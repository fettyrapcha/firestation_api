from django.db import models


def upload_path(instance, filename):
    return '/'.join(['img', str(instance.username), filename])


# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    img = models.ImageField(blank='True', null='True', upload_to='upload_path')
    report = models.TextField(max_length=350)
