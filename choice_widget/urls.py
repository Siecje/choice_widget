from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from account import views

urlpatterns = patterns('',
    url(r'^$', views.education_form, name='education_form'),
    url(r'^admin/', include(admin.site.urls)),
)
