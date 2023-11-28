from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
# Create your views here.
def home(request,year,month):
    name = "JOHN"
    month = month.title() # Convert lowerCase to upperCase
    # Convert month_name to month_number
    month_number = list(calendar.month_name).index(month)
    return render(request, 'home.html',{
        "name" : name,
        "year" : year,
        "month" : month,
        "month_number" : month_number,
    })