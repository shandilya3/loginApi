from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.hello, name='hello'),
    url(r'^$', views.send_email, name='send_email'),
]
