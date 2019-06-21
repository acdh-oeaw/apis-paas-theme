import django_tables2 as tables
from django_tables2.utils import A

from apis_core.apis_entities.models import Person


class PersonTable(tables.Table):

    name = tables.LinkColumn(
        'theme:person-detail',
        args=[A('id')], verbose_name='Name'
    )

    class Meta:
        model = Person
        sequence = ('name', 'first_name', )
        attrs = {"class": "table table-responsive table-hover"}
