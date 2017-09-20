from haystack import indexes
from archives.models import TransationEvents


class TransactionEventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    artist = indexes.CharField(model_attr="artist", faceted=True)
    genre = indexes.CharField(model_attr="work", faceted=True)

    def prepare_artist(self, obj):
        return '%s, %s' % (obj.artist.family_name, obj.artist.first_name)

    def prepare_genre(self, obj):
        if obj.work.genre:
            return '%s' % obj.work.genre.name
        else:
            return 'Unidentified'

    def get_model(self):
        return TransationEvents

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
