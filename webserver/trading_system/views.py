from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required()
def home_view(request):

    return render(request, 'trading_system/home.html')

@login_required()
def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/')