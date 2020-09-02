from django.shortcuts import render , get_object_or_404 , redirect
from django.forms import modelform_factory
# Create your views here.
from meeting.models import Meetings , Room


def detail(request,id):
    meeting = get_object_or_404(Meetings, pk= id)
    return render(request,"meeting/detail.html",{"meeting":meeting})

def rooms_list(request):
    return render(request, "meeting/rooms_list.html",{"rooms":Room.objects.all()})

MeetingForm = modelform_factory(Meetings,exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meeting/new.html", {"form": form})

