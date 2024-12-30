from django import template
from app.models import Category

register = template.Library()

@register.simple_tag
def get_all_objects():
    return Category.objects.all().only("name", "slug")
