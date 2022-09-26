from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag("blog/popular_posts.html")
def get_popular(count=3):
    posts = Post.objects.order_by('-views')[:count]

    return {"posts": posts}


@register.inclusion_tag("blog/tags_tpl.html")
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}