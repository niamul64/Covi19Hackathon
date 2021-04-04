from django.shortcuts import render

# Create your views here.
import serial
from gps import *
def location(request):

    session = gps()  # assuming gpsd running with default options on port 2947
    session.stream(WATCH_ENABLE | WATCH_NEWSTYLE)
    report = session.next()


    return render(request, 'location.html',{'location':report})



