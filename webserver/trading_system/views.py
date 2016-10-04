from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
	return render(request, 'trading_system/home.html')

@login_required
def logout(request):
	logout(request)
	return HttpResponseRedirect('/')