from datetime import date, timedelta
from django.db.models import Q

from apis_core.apis_entities.models import Person

oebl_persons = Person.objects.exclude(Q(text=None) | Q(text__text=""))

current_date = date.today()
current_date = current_date - timedelta(days=1)
current_day = current_date.day
current_month = current_date.month


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
