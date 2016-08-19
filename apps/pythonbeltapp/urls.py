from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^create$', views.create, name="create"),
    url(r'^destination/(?P<trip_id>\d+)$', views.show, name = "show"),
    # url(r'^update/(?P<trip_id>\d+)$', views.update, name="update")
    ]
