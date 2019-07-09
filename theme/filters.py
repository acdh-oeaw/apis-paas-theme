import django_filters
from dal import autocomplete

from apis_core.apis_entities.models import Person
from apis_core.apis_vocabularies.models import ProfessionType

from . utils import oebl_persons
from . filter_utils import born_in_filter, died_in_filter
from . widgets import NoUISliderInput



class PersonListFilter(django_filters.FilterSet):
    place_of_birth = django_filters.CharFilter(
        lookup_expr='icontains',
        field_name='related_place__name',
        method=born_in_filter,
        label="Geburtsort",
        help_text="Zeichenkette die Namen des Geburtsortes enthalten sein sollte"
    )
    place_of_death = django_filters.CharFilter(
        lookup_expr='icontains',
        field_name='related_place__name',
        method=died_in_filter,
        label="Sterbeort",
        help_text="Zeichenkette die Namen des Sterbeortes enthalten sein sollte"
    )
    id = django_filters.NumberFilter(
        label="Name",
        widget=autocomplete.ListSelect2(
            url='theme:obel-person-autocomplete',
            attrs={
                'data-placeholder': 'Suche...',
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
        widget=NoUISliderInput(attrs={
            "date_min": "1799-01-01",
            "date_max": "1850-01-01"
        }),
    )


    end_date = django_filters.DateFromToRangeFilter(
        label="Sterbedatum (Zeitraum)",
        widget=NoUISliderInput(attrs={
            "date_min":"1815-01-01",
            "date_max":"1950-01-01"
        }),
        
    )

    # start_date = django_filters.DateFromToRangeFilter(
    #     label="Geburtsdatum (Zeitraum)",
    #     help_text="Eingabe eines Zeitraumes YYYY-MM-DD - YYYY-MM-DD",
    # )
    # end_date = django_filters.DateFromToRangeFilter(
    #     label="Sterbedatum (Zeitraum)",
    #     help_text="Eingabe eines Zeitraumes YYYY-MM-DD - YYYY-MM-DD",
    # )

    class Meta:
        model = Person
        fields = "__all__"
