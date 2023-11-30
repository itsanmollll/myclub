from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.
def home(request,year=datetime.now().year,month=datetime.now().strftime()):
    name = "JOHN"
    month = month.title() # Convert lowerCase to upperCase
    # Convert month_name to month_number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create calander
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

    # Get Current Year
    now = datetime.now()
    current_year = now.year

    # Get Current time
    time = now.strftime('%I:%M %p')
    return render(request, 'home.html',{
        "name" : name,
        "year" : year,
        "month" : month,
        "month_number" : month_number,
        "cal" : cal,
        "now" : now,
        "current_year" : current_year,
        "time" : time,
    })