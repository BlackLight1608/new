from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    url(r'^$',TemplateView.as_view(template_name="home.html")),
    url(r'^upload/',views.upload_file , name= 'upload_file'),
    url(r'^analyze/',views.change, name='change'),
    url(r'^media/step2.xlsx$',TemplateView.as_view(template_name="final.html")),
    url(r'^update/',views.update, name='update'),
]
