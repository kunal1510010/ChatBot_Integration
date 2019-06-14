from . import views
from django.conf.urls import url

app_name = 'ChatTest'

urlpatterns = [
        url(r'^test/$', views.main, name='main')
]
