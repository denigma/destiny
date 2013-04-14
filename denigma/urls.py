from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import HomeView, AboutView, ContactView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
)
