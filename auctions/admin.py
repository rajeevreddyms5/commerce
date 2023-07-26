from django.contrib import admin
from .models import User, Listings, Bids, Comments

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category", "listedby", "status")

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("comments", "commentsby")
    
class BidsAdmin(admin.ModelAdmin):
    list_display = ("bidby", "bidlisting", "bidplaced")




# Register your models here.
admin.site.register(User)
admin.site.register(Listings, ListingAdmin)
admin.site.register(Bids, BidsAdmin)
admin.site.register(Comments, CommentsAdmin)
