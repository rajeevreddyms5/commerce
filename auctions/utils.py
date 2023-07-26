from django.db.models import Max
from .models import User, Listings, Bids, Comments


# get highest bid price in a list
def max_price(id):
    return Bids.objects.filter(bidlisting=id).aggregate(Max('bidplaced')).get('bidplaced__max')