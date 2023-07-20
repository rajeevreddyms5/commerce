from django.contrib import admin
from .models import User, Listings, Bids, Comments

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category", "listedby")

# Register your models here.
admin.site.register(User)
admin.site.register(Listings, ListingAdmin)
admin.site.register(Bids)
admin.site.register(Comments)
