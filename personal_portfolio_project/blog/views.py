from django.shortcuts import render
from django.http import HttpResponse

def all_blogs(request):
    return render(request, 'blog/all_blogs.html')

def Tunde(request):
    return HttpResponse('THIS IS IT')
