from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils.datetime_safe import datetime

from meeting.models import Meetings


def welcome(requset):
    return render(requset, "website/welcome.html" ,{
                  "meetings": Meetings.objects.all()})

def date(request):
    return HttpResponse('this page was served at' + str(datetime.now()))