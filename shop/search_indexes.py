from haystack import indexes
from .models import Store


class StoreIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    store_name = indexes.CharField(model_attr='store_name')

    def get_model(self):
        return Store

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
