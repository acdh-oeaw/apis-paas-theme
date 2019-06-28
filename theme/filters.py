import django_filters
from dal import autocomplete

from apis_core.apis_entities.models import Person
from apis_core.apis_vocabularies.models import ProfessionType

from . utils import oebl_persons


class PersonListFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(
        label="Autocomplete-Suche",
        help_text="Autocomplete-Suche",
        widget=autocomplete.ListSelect2(
            url='theme:obel-person-autocomplete',
            attrs={
                'data-placeholder': 'Subak...',
                'data-minimum-input-length': 3,
            },
        ),
    )
    profession = django_filters.ModelMultipleChoiceFilter(
        label="Berufe",
        queryset=ProfessionType.objects.all(),
        help_text="Berufe und Berufsgruppen (autocomplete)",
        widget=autocomplete.Select2Multiple(
            url='theme:obel-professions-autocomplete',
            attrs={
                'data-placeholder': 'Unterrichtswesen...',
                'data-minimum-input-length': 3,
            },
        ),
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Nachname",
        help_text="Zeichenkette die im Nachnamen enthalten sein muss",
    )
    first_name = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Vorname",
        help_text="Zeichenkette die im Vornamen enthalten sein muss",
    )
    start_date = django_filters.DateFromToRangeFilter(
        label="Geburtsdatum (Zeitraum)",
        help_text="Eingabe eines Zeitraumes YYYY-MM-DD - YYYY-MM-DD",
    )
    end_date = django_filters.DateFromToRangeFilter(
        label="Sterbedatum (Zeitraum)",
        help_text="Eingabe eines Zeitraumes YYYY-MM-DD - YYYY-MM-DD",
    )

    class Meta:
        model = Person
        fields = "__all__"
