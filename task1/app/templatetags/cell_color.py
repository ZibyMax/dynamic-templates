from django import template

register = template.Library()


@register.filter
def cell_color(value):
    if value:
        value = float(value)
        if value < 0:
            return 'Green'
        elif value > 5:
            return 'Red'
        elif value > 3:
            return 'LightCoral'
        elif value > 1:
            return 'LightPink'
    return 'White'
