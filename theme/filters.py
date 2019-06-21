import django_filters
from dal import autocomplete

from apis_core.apis_entities.models import Person


class PersonListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('name').help_text,
        label=Person._meta.get_field('name').verbose_name
        )

    class Meta:
        model = Person
        fields = "__all__"
