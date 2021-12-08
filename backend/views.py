from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import StudentSerializer


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        img = request.data['img']
        username = request.data['username']
        location = request.data['location']
        report = request.data['report']
        Student.objects.create(img=img,
                               username=username,
                               location=location,
                               report=report)
        return HttpResponse({'feedback': "information sent successdfully"},
                            status=200)
