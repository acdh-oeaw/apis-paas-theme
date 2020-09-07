from rest_framework.generics import ListAPIView
from haystack.query import SearchQuerySet
from .forms import PersonFacetedSearchForm
from apis_core.api_routers import serializers_dict
from apis_core.apis_relations.models import PersonInstitution
from apis_core.api_renderers import NetJsonRenderer


class NetVizTheme(ListAPIView):
    action = 'list'
    renderer_classes = [NetJsonRenderer]


    def get_serializer_class(self):
        return serializers_dict['PersoninstitutionSerializer']

    def get_queryset(self):
        kwargs = {"load_all": True, "searchqueryset": SearchQuerySet()}
        sqs1 = PersonFacetedSearchForm(self.request.GET, **kwargs).search()
        pi = PersonInstitution.objects.filter(related_person_id__in=[x.pk for x in sqs1])
        return pi



