from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'today-news.html', {"date": date,})

    

def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    day = days[day_number]
    return day

def news_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

