from haystack import indexes
from django.conf import settings

from apis_core.apis_metainfo.models import Text
from apis_core.apis_vocabularies.models import LabelType
from apis_core.apis_labels.models import Label
from .utils import oebl_persons
from apis_core.apis_entities.models import Person


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField()
    birth_date = indexes.DateField(model_attr='start_date', null=True, faceted=True)
    death_date = indexes.DateField(model_attr='end_date', null=True, faceted=True)
    birth_date_show = indexes.CharField(model_attr='start_date_written', null=True)
    death_date_show = indexes.CharField(model_attr='end_date_written', null=True)
    place_of_birth = indexes.CharField(null=True, faceted=True)
    place_of_death = indexes.CharField(null=True, faceted=True)
    gender = indexes.CharField(null=True, model_attr="gender", faceted=True)
    profession = indexes.MultiValueField(null=True, faceted=True)
    education = indexes.MultiValueField(null=True, faceted=True)
    career = indexes.MultiValueField(null=True, faceted=True)
     
    def get_model(self):
        return Person
    
    def prepare_name(self, object):
        return str(object)
    
    def prepare_text(self, object):
        txt_types = getattr(settings, 'APIS_SEARCH_TEXTTYPES', [])
        res = {'first_name': object.first_name, 'name': object.name}
        alt_names = getattr(settings, 'APIS_ALTERNATIVE_NAMES', [])
        alt_names_qs = LabelType.objects.filter(name__in=alt_names)
        res['alternative_names'] = [alt.label for alt in Label.objects.filter(temp_entity=object, label_type__in=alt_names_qs)]
        res['texts'] = []
        for txt in object.text.filter(kind__name__in=txt_types):
            res['texts'].append(txt.text)
        return res
    
    def prepare_profession(self, object):
        return [x.label for x in object.profession.all()]
    
    def prepare_place_of_birth(self, object):
        rel = object.personplace_set.filter(relation_type_id=595)
        if rel.count() == 1:
            return rel[0].related_place.name
        else:
            return None

    def prepare_place_of_death(self, object):
        rel = object.personplace_set.filter(relation_type_id=596)
        if rel.count() == 1:
            return rel[0].related_place.name
        else:
            return None
    
    def prepare_education(self, object):
        lst_edu = getattr(settings, "APIS_SEARCH_EDUCATION", [])
        res = []
        for x in object.personinstitution_set.all():
            lst_lbls = [y.strip() for y in x.relation_type.label.split('>>')]
            for l in lst_lbls:
                if l in lst_edu:
                    if x.related_institution.name not in res:
                        res.append(x.related_institution.name)
        for x in object.personplace_set.all():
            lst_lbls = [y.strip() for y in x.relation_type.label.split('>>')]
            for l in lst_lbls:
                if l in lst_edu:
                    if x.related_place.name not in res:
                        res.append(x.related_place.name)
        return res

    def prepare_career(self, object):
        lst_edu = getattr(settings, "APIS_SEARCH_CAREER", [])
        res = []
        for x in object.personinstitution_set.all():
            lst_lbls = [y.strip() for y in x.relation_type.label.split('>>')]
            for l in lst_lbls:
                if l in lst_edu:
                    if x.related_institution.name not in res:
                        res.append(x.related_institution.name)
        for x in object.personplace_set.all():
            lst_lbls = [y.strip() for y in x.relation_type.label.split('>>')]
            for l in lst_lbls:
                if l in lst_edu:
                    if x.related_place.name not in res:
                        res.append(x.related_place.name)
        return res

    def index_queryset(self, using=None):
        return oebl_persons

