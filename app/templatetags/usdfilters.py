from django import template
register = template.Library()
def swap(value):
    return value.swapcase()


@register.filter(name='remove')
def rem(value,char):
    return value.replace(char,'')

register.filter('swapcase',swap) # we can use decorater like @register.filter(name ='filterName)