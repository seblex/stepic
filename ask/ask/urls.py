from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'ask.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

      url(r'^', include('qa.urls')),
#     #url(r'^admin/', include(admin.site.urls)),
)


# urlpatterns = patterns('qa.views',                                              
#    url(r'^$', 'test'),                                                          
#    url(r'^login/.*$', 'test', name='login'),                                    
#    url(r'^signup/.*', 'test', name='signup'),                                   
#    url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),                 
#    url(r'^ask/.*', 'test', name='ask'),                                         
#    url(r'^popular/.*', 'test', name='popular'),                                 
#    url(r'^new/.*', 'test', name='new'),                                         
# )    