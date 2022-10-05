from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app_uday(request):
    return HttpResponse('<h1><center><i><marquee><mark>i am uday</center></mark></marquee></i></h1>')