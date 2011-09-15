from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def richcomments_static():
    return render_to_string('richcomments/templatetags/richcomments_static.html')
