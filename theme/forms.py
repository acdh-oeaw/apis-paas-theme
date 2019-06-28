from django import forms
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup

from apis_core.apis_entities.models import Person


class PersonSearchForm(forms.Form):
    search_field = forms.ChoiceField(widget=autocomplete.Select2ListView(
        url='theme:obel-person-autocomplete')
    )


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
                'Basic search options',
                'name',
                'forename',
                'written_name',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Biographisches',
                    'profession',
                    'gender',
                    css_id="more"
                    ),
                AccordionGroup(
                    'Rolle',
                    'first_name',
                    'is_related',
                    'is_adm',
                    'is_other',
                    css_id="rolle"
                    ),
                AccordionGroup(
                    'Anmerkungen',
                    'notes',
                    'collection',
                    css_id="inventare"
                    ),
                )
            )
