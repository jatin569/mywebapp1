from django.conf.urls import url,include
from . import views
urlpatterns = [
  url(r'^$', views.index,name="index1"),
  url(r'^registration/$',views.reg,name='reg1'),
  url(r'^login/$', views.login, name='login1'),
  url(r'^logout/$', views.logout, name='logout1'),
    ]