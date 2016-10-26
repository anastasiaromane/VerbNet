from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^verbs/$', views.verbs, name='verbs'),
    url(r'^graphs/$', views.graphs, name='graphs'),
    url(r'^verbnet/$', views.verbnet, name='verbnet'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.sendemail, name='contacts'),
    # url(r'^thanks/$', views.thanks, name='thanks'),
]