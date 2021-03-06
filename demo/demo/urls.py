from django.conf.urls import patterns, include, url
import webapp.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$', webapp.views.ListContactView.as_view(),name='contacts-list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add$', webapp.views.CreateContactView.as_view(),name='contacts-new'),
    url(r'^edit/(?P<pk>\d+)$', webapp.views.ContacteditView.as_view(),name='contacts-new1'),
    url(r'^delete/(?P<pk>\d+)$', webapp.views.ContactDelete.as_view(),name='contacts-delete'),
)
