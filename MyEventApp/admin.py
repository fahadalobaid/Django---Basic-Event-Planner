from django.contrib import admin
from .models import Event

# Register your models here.

admin.site.register(Event)
class PostAdmin(admin.ModelAdmin):
    fields = ("organizer" ,"name",  "email", "image"  ,"num_of_seats"  ,"booked_seats",  "start_date" , "end_date","id")