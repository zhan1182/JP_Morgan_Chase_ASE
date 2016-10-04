from django.conf.urls import url

from trading_system import views

urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'^logout/', views.logout, name='logout'),
]
