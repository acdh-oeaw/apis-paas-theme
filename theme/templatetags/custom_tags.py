from django import template
from theme.utils import oebl_persons
register = template.Library()

@register.simple_tag
def people_count():
    return oebl_persons.count()


@register.simple_tag
def formated_daterange(startdate, enddate):
    rangestring = ''
    if (startdate and startdate is not None) or (enddate and enddate is not None):
        rangestring += '('
        if (startdate and startdate is not None):
            rangestring += startdate
        if (enddate and enddate is not None):
            rangestring += '-' + enddate
        rangestring += ')'
    return rangestring

    