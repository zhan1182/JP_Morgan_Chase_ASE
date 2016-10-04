from django.conf.urls import url

from index_app import views

urlpatterns = [
    url(r'', views.index, name='index'),
]
