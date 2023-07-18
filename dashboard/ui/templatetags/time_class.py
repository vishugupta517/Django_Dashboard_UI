from django import template

register = template.Library()

TIME = 3600


@register.filter
def time_class(value):
    try:
        time_value = int(value)
    except (ValueError, TypeError):
        return ""

    if time_value < TIME:
        return "green-time"
    else:
        return "red-time"
