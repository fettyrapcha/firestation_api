from django.contrib import admin

from .serializers import StudentSerializer
from .models import *
# Register your models here.
admin.site.register(Student)
