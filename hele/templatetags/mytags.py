from django import template

register = template.Library()
@register.filter
def roundfunc(value):
    if value== None:
        return 0;
    else:
        return int(int(value*1000+0.5)/10)/100