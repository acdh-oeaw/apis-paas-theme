import django_filters
from django.template import loader
from django import forms


class NoUISliderInput(django_filters.widgets.RangeWidget):
    template_name = 'utils/slider.html'
    attr_names = ('date_min', 'date_max')

    class Media:
        css = {'all': ('theme/vendor/noUISlider/nouislider.min.css',
                       'theme/css/slider_custom.css',)}
        js = ("theme/vendor/noUISlider/nouislider.min.js",
              "theme/vendor/wNumb/wNumb.js",)

    def __init__(self, widgets=None, attrs=None):
        if widgets is None:
            widgets = (forms.TextInput, forms.TextInput)
        # NOTE: skip parent init
        super(django_filters.widgets.RangeWidget, self).__init__(widgets,
                                                                 attrs)
