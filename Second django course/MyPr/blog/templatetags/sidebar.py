from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag("blog/popular_posts.html")
def get_popular(count=3):
    posts = Post.objects.order_by('-views')[:count]

    return {"posts": posts}
