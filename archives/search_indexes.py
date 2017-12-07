from haystack import indexes
from archives.models import TransationEvents


class TransactionEventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    artist = indexes.CharField(model_attr="artist", faceted=True, null=True)
    genre = indexes.CharField(model_attr="work", faceted=True)
    stock_number = indexes.CharField(model_attr="stock_number")
    work = indexes.CharField(model_attr="work")
    buyer = indexes.CharField(faceted=True)
    seller = indexes.CharField(faceted=True)

    def prepare_buyer(self, obj):
        if obj.buyer:
            return '%s' % (obj.buyer.family_name)
        else:
            return "Unidentified"

    def prepare_seller(self, obj):
        if obj.seller:
            return '%s' % (obj.seller.family_name)
        else:
            return 'Unidentified'

    def prepare_work(self, obj):
        return '%s' % obj.work.title

    def prepare_stock_number(self, obj):
        return str(obj.stock_number)

    def prepare_artist(self, obj):
        if obj.artist:
            return '%s, %s' % (obj.artist.family_name, obj.artist.first_name)
        else:
            return 'Not specified'

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
