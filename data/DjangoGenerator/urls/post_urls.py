from django.conf.urls import patterns, url
from ..views import (PostListView, PostCreateView, PostDetailView,
                     PostUpdateView, PostDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(PostCreateView.as_view()),
        name="post_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PostUpdateView.as_view()),
        name="post_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PostDeleteView.as_view()),
        name="post_delete"),

    url(r'^(?P<pk>\d+)/$',
        PostDetailView.as_view(),
        name="post_detail"),

    url(r'^$',
        PostListView.as_view(),
        name="post_list"),
)
