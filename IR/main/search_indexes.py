from haystack import indexes
from .models import FanFiction

class FanFictionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    author = indexes.CharField(model_attr='author')
    movie = indexes.CharField(model_attr='movie')

    def get_model(self):
        return FanFiction
