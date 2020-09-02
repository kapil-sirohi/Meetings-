from django.contrib import admin

# Register your models here.
from .models import Meetings , Room

admin.site.register(Meetings)
admin.site.register(Room)