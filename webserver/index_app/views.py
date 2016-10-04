from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.


def index(request):

    return render(request, 'index/index.html')


def login(request):

    if request.method == 'POST':
        
        return HttpResponseRedirect('/home/')

    else:
        raise Http404()


def register(request):

    if request.method == 'POST':
        
        return HttpResponseRedirect('/')

    else:
        return render(request, 'index/register.html')