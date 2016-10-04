from django.conf.urls import url

from trading_system import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^logout/', views.logout_view, name='logout'),
]
