from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):

    return render(request, 'index/index.html')


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponse('Failed to log in! Please return to the previous page.')

    else:
        raise Http404()


def register(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        print username, password, email

        user = User.objects.create_user(username, email, password)
        user.save()

        return HttpResponseRedirect('/')

    else:
        return render(request, 'index/register.html')