from django import template
register = template.Library()
from  theme.utils import oebl_persons

@register.simple_tag
def people_count():
    return oebl_persons.count()