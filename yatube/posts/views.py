from django.shortcuts import render, get_object_or_404

from .models import Post, Group

MAGIC_NUMBER = 10  # Number of posts in a page.


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by(
        '-pub_date')[:MAGIC_NUMBER]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
