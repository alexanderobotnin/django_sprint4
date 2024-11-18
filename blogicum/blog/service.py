from django.core.paginator import Paginator
from django.db.models import Count
from django.utils import timezone

from .constants import POSTS_BY_PAGE
from .models import Post


def get_posts(post_objects=Post.objects, include_hidden=False):
    """Посты из БД."""
    post_objects = post_objects.annotate(
            comment_count=Count('comments')).select_related(
                'author', 'category', 'location').order_by('-pub_date')
    if include_hidden:
        return post_objects
    return post_objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True)


def get_paginator(request, items, num=POSTS_BY_PAGE):
    """Создает объект пагинации."""
    return Paginator(items, num).get_page(request.GET.get('page'))
