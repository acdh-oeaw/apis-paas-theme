import datetime
from haystack import indexes

from apis_core.apis_metainfo.models import Text

from . utils import oebl_persons


class TextIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Text

    def index_queryset(self, using=None):
        #oebl_texts = [x.text.all()[0].id for x in oebl_persons]
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(tempentityclass__in=oebl_persons)
