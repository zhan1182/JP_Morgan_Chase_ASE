from django.conf.urls import url

from index_app import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^login/', views.login_view, name='login'),
]
