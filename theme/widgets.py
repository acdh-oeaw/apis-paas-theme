import django_filters
from django.template import loader

class NoUISliderInput(django_filters.widgets.RangeWidget):
    template_name = 'utils/slider.html'
    attr_names = ('start', 'end')


    class Media:
        css = {'all':('theme/vendor/noUISlider/nouislider.min.css',
            'theme/css/slider_custom.css',)}
        js = ("theme/vendor/noUISlider/nouislider.min.js",
              "theme/vendor/wNumb/wNumb.js",)

    def __init__(self,attrs):
        super(NoUISliderInput, self).__init__(attrs)


    def value_from_datadict(self, data, files, name):
        return [widget.value_from_datadict(data, files,
                                           name + '_%s' % self.attr_names[i])
                for i, widget in enumerate(self.widgets)]
