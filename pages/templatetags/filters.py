from django import template

register = template.Library()


@register.filter
def subtract(value, arg):
    return "{:.2f}".format(value - arg)
