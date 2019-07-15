from . import views
from django.conf.urls import url

app_name = 'ChatTest'

urlpatterns = [
        url(r'^$', views.main, name='main'),
        url(r'^input/$', views.input_ans, name='input ans')
]
