from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import UpdateView, ListView, FormView
from extra_views import ModelFormSetView
from requests import request

from bolt_usersite.forms import BlogForm
from .models import *
from helpers.wordpress_upload import xmlrpc_object

BoltUser = get_user_model()


class IndexView(ListView):
    context_object_name = 'index'
    template_name = 'bolt_usersite/main.html'
    model = BoltUser

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['Post'] = Blog.objects.all()
        return context


class ProfileView(UpdateView):
    context_object_name = 'profile'
    template_name = 'bolt_usersite/profile.html'
    model = BoltUser
    fields = [
        'email',
        'password',
        'first_name',
        'last_name',
        'wordpress_link',
        'wordpress_id',
        'wordpress_pass'
    ]

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

    def get_initial(self):
        return self.request.GET

    def get_success_url(self, **kwargs):
        return reverse_lazy('bolt_usersite:profile', kwargs={'pk': self.object.pk})


class CreatePostView(FormView):
    context_object_name = 'createpost'
    template_name = 'bolt_usersite/blog/create_post.html'
    form_class = BlogForm
    success_url = reverse_lazy('bolt_usersite:index')

    def get_context_data(self, **kwargs):
        context = super(CreatePostView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = self.request.user
        link = "http://" + user.wordpress_link + "/xmlrpc.php"
        title = form.cleaned_data['title']
        category_object = form.cleaned_data['category']
        category = title_list(category_object)
        tag_object = form.cleaned_data['tag']
        tag = title_list(tag_object)
        content = form.cleaned_data['body']
        xmlrpc_object.post_article(link, user.wordpress_id, user.wordpress_pass, title, category,
                                   content, tag)
        form.save()
        return super(CreatePostView, self).form_valid(form)


def title_list(objects):
    listing = []
    for item in objects:
        listing.append(item.title)

    return listing
