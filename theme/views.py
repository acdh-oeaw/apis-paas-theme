import requests

from django.views.generic import TemplateView

from django.views.generic.detail import DetailView
from browsing.browsing_utils import GenericListView

from apis_core.apis_entities.models import Person
from webpage.views import get_imprint_url
from . filters import PersonListFilter
from . forms import PersonFilterFormHelper
from . tables import PersonTable


class ImprintView(TemplateView):
    template_name = 'theme/imprint.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        imprint_url = get_imprint_url()
        r = requests.get(get_imprint_url())

        if r.status_code == 200:
            context['imprint_body'] = "{}".format(r.text)
        else:
            context['imprint_body'] = """
            On of our services is currently not available. Please try it later or write an email to
            acdh@oeaw.ac.at; if you are service provide, make sure that you provided ACDH_IMPRINT_URL and REDMINE_ID
            """
        return context


class IndexView(TemplateView):
    template_name = 'theme/index.html'


class AboutView(TemplateView):
    template_name = 'theme/about.html'


class PersonListView(GenericListView):
    model = Person
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    table_class = PersonTable
    template_name = 'theme/generic_list.html'
    init_columns = [
        'name',
        'first_name',
    ]


class PersonDetailView(DetailView):
    model = Person
    template_name = 'theme/person_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['prev'] = self.model.objects.filter(
                id__lt=self.object.id
            ).order_by("-id").first()
        except AttributeError:
            context['prev'] = None
        try:
            context['next'] = self.model.objects.filter(id__gt=self.object.id).first()
        except AttributeError:
            context['next'] = None
        main_text = self.object.text.all()[0].text
        context['main_text'] = main_text

        return context
