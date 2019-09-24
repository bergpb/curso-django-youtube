from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('Hello word!')


def taskList(request):
    return render(request, 'tasks/lists.html')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})