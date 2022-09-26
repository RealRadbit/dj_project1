from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag("blog/pagination.html")
def get_pages():
    posts = Post.objects.order_by('-views')

    return {"posts": posts}
