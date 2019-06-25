import requests
import datetime
import random
import copy

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
    model = Person
    template_name = 'theme/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        peoplebornthisday = self.model.objects.filter(start_date__day = datetime.datetime.now().day,start_date__month = datetime.datetime.now().month)
        peoplediedthisday = self.model.objects.filter(end_date__day = datetime.datetime.now().day,end_date__month = datetime.datetime.now().month)
        randompersonbornthisday = random.choice(peoplebornthisday)
        randompersondiedthisday = random.choice(peoplediedthisday)
        setattr(randompersonbornthisday,'desc',randompersonbornthisday.text.all()[0].text)
        setattr(randompersondiedthisday,'desc',randompersondiedthisday.text.all()[0].text)
        randomentries = random.sample(list(self.model.objects.all()),2)

        for randomentry in randomentries:
            setattr( randomentry,'desc', randomentry.text.all()[0].text)

        context['randomentries'] = randomentries
        context['randombornthisday'] = randompersonbornthisday
        context['randomdiedthisday'] = randompersondiedthisday
        context['randombornthisday_desc'] = context['randombornthisday'].text.all()[0].text
        context['randomdiedthisday_desc'] = context['randomdiedthisday'].text.all()[0].text

        return context

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


