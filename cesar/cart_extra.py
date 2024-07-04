from django import template

register = template.Library()

@register.simple_tag
def sum_cantidad(carrito):
    total_cantidad = sum(item['acumulado'] for item in carrito.values())
    return total_cantidad