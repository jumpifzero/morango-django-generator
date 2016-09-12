from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Post
from ..forms import PostForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PostListView(ListView):
    model = Post
    template_name = "webapp/post_list.html"
    paginate_by = 20
    context_object_name = "post_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PostListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PostListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PostListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PostListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PostListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PostListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PostListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PostListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PostListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PostListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PostListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PostListView, self).get_template_names()


class PostDetailView(DetailView):
    model = Post
    template_name = "webapp/post_detail.html"
    context_object_name = "post"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PostDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PostDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PostDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PostDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PostDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PostDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PostDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PostDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PostDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PostDetailView, self).get_template_names()


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    fields = ['title', 'author', 'body', 'publishDate']
    template_name = "webapp/post_create.html"
    success_url = reverse_lazy("post_list")

    def __init__(self, **kwargs):
        return super(PostCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PostCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PostCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PostCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PostCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(PostCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PostCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PostCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PostCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PostCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PostCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PostCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PostCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("post_detail", args=(self.object.pk,))


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    fields = ['title', 'author', 'body', 'publishDate']
    template_name = "webapp/post_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "post"

    def __init__(self, **kwargs):
        return super(PostUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PostUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PostUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PostUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PostUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PostUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PostUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PostUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(PostUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PostUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PostUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PostUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PostUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PostUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PostUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PostUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PostUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("post_detail", args=(self.object.pk,))


class PostDeleteView(DeleteView):
    model = Post
    template_name = "webapp/post_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "post"

    def __init__(self, **kwargs):
        return super(PostDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PostDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PostDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PostDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PostDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PostDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PostDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PostDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PostDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PostDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("post_list")
