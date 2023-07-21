from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create", views.create, name="create"),
    path("listings/<int:id>", views.listing_page, name="listing_page"),
    path("watcha/<int:id>", views.add_watch, name="add_watch"),
    path("watchr/<int:id>", views.remove_watch, name="remove_watch"),
    path("bid", views.bid, name="bid")
]
