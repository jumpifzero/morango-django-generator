from django.conf.urls import patterns, url
from ..views import (TagListView, TagCreateView, TagDetailView,
                     TagUpdateView, TagDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(TagCreateView.as_view()),
        name="tag_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(TagUpdateView.as_view()),
        name="tag_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(TagDeleteView.as_view()),
        name="tag_delete"),

    url(r'^(?P<pk>\d+)/$',
        TagDetailView.as_view(),
        name="tag_detail"),

    url(r'^$',
        TagListView.as_view(),
        name="tag_list"),
)
