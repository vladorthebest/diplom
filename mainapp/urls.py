from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('startet', views.new_etalon),
    url('parse', views.new_day),
    url('create', views.classroom_create),
    url('^(?P<pk>\d+)$', views.LessonDetailView.as_view(), name = 'lesson_detail'),
    url('day', views.main),
    url('^$', views.main_list),
    url('^etalon$', views.main_e),
    url('etalon/(?P<pk>\d+)$', views.EtalonDetailView.as_view(), name = 'lessone_detail'),
    url('info', views.info)
]



