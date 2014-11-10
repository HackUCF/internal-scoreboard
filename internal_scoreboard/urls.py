from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'internal_scoreboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'content.views.index', name='index'),

    url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^scoreboard$', 'competitions.views.scoreboard', name='competitions.scoreboard'),
    url(r'^competitions/$', 'competitions.views.competitions', name='competitions.competitions'),
    url(r'^competitions/(?P<slug>[\w\d\-]+)/$', 'competitions.views.competition', name='competitions.competition'),
)

