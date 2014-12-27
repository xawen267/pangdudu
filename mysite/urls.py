from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.view import hello,homepage,ctime,current_datetime
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url('^$','pachong.views.index'),
    url(r'^time/(\d{1,2})/$',ctime),
    url(r'^current_datetime/$',current_datetime),
    url(r'^blog/index/(?P<id>\d{2})/$','pachong.views.index'),
)
