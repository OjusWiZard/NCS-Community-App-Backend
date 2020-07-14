from django.shortcuts import render
from django.http import HttpResponse
from .models import Venue, Lab, Attendance

def markAttendance(request,venue):
    return HttpResponse("Pass")