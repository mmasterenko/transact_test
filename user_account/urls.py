from django.conf.urls import url
from user_account import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^validate$', views.validate, name='validate'),
    url(r'^transact$', views.do_transact, name='transact'),
]
