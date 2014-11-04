from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'internal_scoreboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'content.views.index'),
    url(r'^competition/(?P<slug>[\w\d\-]+)/', 'competitions.views.competition', name='competitions.competition')
)
