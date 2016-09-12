from django.conf.urls import patterns, url
from ..views import (AuthorListView, AuthorCreateView, AuthorDetailView,
                     AuthorUpdateView, AuthorDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(AuthorCreateView.as_view()),
        name="author_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AuthorUpdateView.as_view()),
        name="author_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AuthorDeleteView.as_view()),
        name="author_delete"),

    url(r'^(?P<pk>\d+)/$',
        AuthorDetailView.as_view(),
        name="author_detail"),

    url(r'^$',
        AuthorListView.as_view(),
        name="author_list"),
)
