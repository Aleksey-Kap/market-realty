from django import template
register = template.Library()

@register.filter
def dictkey(dict, key):
    try:
        return dict[key]
    except KeyError:
        return ''