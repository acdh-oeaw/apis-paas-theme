from django import forms
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup

from apis_core.apis_entities.models import Person
from . utils import oebl_persons


class PersonFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PersonFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                '',
                'id',
                'name',
                'first_name',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Lebensdaten',
                    'start_date',
                    'end_date',
                    css_id="lebensdaten"
                    ),
                AccordionGroup(
                    'Geburts- und Sterbeort',
                    'place_of_birth',
                    'place_of_death',
                    css_id="geburtsort"
                    ),
                AccordionGroup(
                    'Beruf und Geschlecht',
                    'profession',
                    'gender',
                    css_id="more"
                    ),
                AccordionGroup(
                    'Anmerkungen',
                    'notes',
                    'collection',
                    css_id="inventare"
                    ),
                )
            )
