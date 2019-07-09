from datetime import date, timedelta
from django.db.models import Q

from apis_core.apis_entities.models import Person
from apis_core.apis_relations.models import PersonPlace

oebl_persons = Person.objects.exclude(Q(text=None) | Q(text__text=""))

oebl_persons_with_date = oebl_persons.exclude(Q(start_date=None) |
                                              Q(end_date=None))

person_place_born = PersonPlace.objects.filter(
    Q(relation_type__name__icontains='birth') | Q(relation_type__name__icontains='geboren')
)
person_place_death = PersonPlace.objects.filter(
    Q(relation_type__name__icontains='death') | Q(relation_type__name__icontains='gestorben')
)

current_date = date.today()
current_date = current_date - timedelta(days=1)
current_day = current_date.day
current_month = current_date.month


def get_born_range():
    oebl_persons_sorted_by_start_date = oebl_persons_with_date.order_by('start_date')
    oldest_person = oebl_persons_sorted_by_start_date.first()
    youngest_person = oebl_persons_sorted_by_start_date.last()
    return [oldest_person.start_date, youngest_person.start_date]


def get_died_range():
    oebl_persons_sorted_by_end_date = oebl_persons_with_date.order_by('end_date')
    person_died_first = oebl_persons_sorted_by_end_date.first()
    person_died_last = oebl_persons_sorted_by_end_date.last()
    return [person_died_first.end_date, person_died_last.end_date]


def get_died_latest():
    person_died_latest = oebl_persons.order_by('-end_date')[1]
    return person_died_latest.end_date


def get_daily_entries(context, qs):
    context['person_born'] = qs.filter(
        start_date__day=current_day,
        start_date__month=current_month
    )
    context['person_born_count'] = context['person_born'].count()
    context['person_died'] = qs.filter(
        end_date__day=current_day,
        end_date__month=current_month
    )
    context['person_died_count'] = context['person_died'].count()
    return context
