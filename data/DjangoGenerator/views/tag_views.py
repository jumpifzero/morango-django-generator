from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Tag
from ..forms import TagForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class TagListView(ListView):
    model = Tag
    template_name = "webapp/tag_list.html"
    paginate_by = 20
    context_object_name = "tag_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(TagListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TagListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TagListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(TagListView, self).get_queryset()

    def get_allow_empty(self):
        return super(TagListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(TagListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(TagListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(TagListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(TagListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(TagListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(TagListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TagListView, self).get_template_names()


class TagDetailView(DetailView):
    model = Tag
    template_name = "webapp/tag_detail.html"
    context_object_name = "tag"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(TagDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TagDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TagDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TagDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(TagDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(TagDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(TagDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TagDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TagDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TagDetailView, self).get_template_names()


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    fields = ['name']
    template_name = "webapp/tag_create.html"
    success_url = reverse_lazy("tag_list")

    def __init__(self, **kwargs):
        return super(TagCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(TagCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TagCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TagCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(TagCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(TagCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(TagCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(TagCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(TagCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TagCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TagCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(TagCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TagCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("tag_detail", args=(self.object.pk,))


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    fields = ['name']
    template_name = "webapp/tag_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "tag"

    def __init__(self, **kwargs):
        return super(TagUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TagUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TagUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TagUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TagUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(TagUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(TagUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(TagUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(TagUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(TagUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(TagUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(TagUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TagUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TagUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TagUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TagUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TagUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("tag_detail", args=(self.object.pk,))


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "webapp/tag_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "tag"

    def __init__(self, **kwargs):
        return super(TagDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TagDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(TagDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(TagDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TagDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(TagDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(TagDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(TagDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TagDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TagDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TagDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("tag_list")
