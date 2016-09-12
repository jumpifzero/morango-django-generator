from django.conf.urls import patterns, include

urlpatterns = patterns('',

    (r'^posts/', include('webapp.urls.post_urls')),  # NOQA
    (r'^tags/', include('webapp.urls.tag_urls')),
    (r'^authors/', include('webapp.urls.author_urls')),
)
