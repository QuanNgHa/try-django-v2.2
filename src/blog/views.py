from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost

# GET -> 1 object
# filter -> [] objects


def blog_post_detail_page(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_detail_page.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    # list out objects:
    # couold be search
    qs = BlogPost.objects.all()  # querry set --> list of python objects
    template_name = "blog/blog_post_list.html"
    context = {'object_list': qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    template_name = "blog/blog_post_create.html"
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {"object": obj}
    return render(request, template_name, context)
