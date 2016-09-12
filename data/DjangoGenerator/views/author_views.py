from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Author
from ..forms import AuthorForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AuthorListView(ListView):
    model = Author
    template_name = "webapp/author_list.html"
    paginate_by = 20
    context_object_name = "author_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AuthorListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthorListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthorListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AuthorListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AuthorListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AuthorListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AuthorListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AuthorListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AuthorListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AuthorListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthorListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthorListView, self).get_template_names()


class AuthorDetailView(DetailView):
    model = Author
    template_name = "webapp/author_detail.html"
    context_object_name = "author"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AuthorDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthorDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthorDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthorDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthorDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthorDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthorDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthorDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthorDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthorDetailView, self).get_template_names()


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    fields = ['name', 'dateOfBirth']
    template_name = "webapp/author_create.html"
    success_url = reverse_lazy("author_list")

    def __init__(self, **kwargs):
        return super(AuthorCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AuthorCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthorCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthorCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AuthorCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(AuthorCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthorCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthorCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthorCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthorCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthorCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AuthorCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthorCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("author_detail", args=(self.object.pk,))


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    fields = ['name', 'dateOfBirth']
    template_name = "webapp/author_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "author"

    def __init__(self, **kwargs):
        return super(AuthorUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthorUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthorUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthorUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthorUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthorUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthorUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AuthorUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(AuthorUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthorUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthorUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthorUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthorUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthorUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthorUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthorUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthorUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("author_detail", args=(self.object.pk,))


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "webapp/author_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "author"

    def __init__(self, **kwargs):
        return super(AuthorDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthorDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AuthorDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AuthorDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthorDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthorDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthorDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthorDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthorDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthorDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthorDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("author_list")
