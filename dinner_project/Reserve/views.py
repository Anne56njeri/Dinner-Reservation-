from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    title="Welcome to reserve"
    return render(request,'Hotel/welcome.html',{"title":title})
