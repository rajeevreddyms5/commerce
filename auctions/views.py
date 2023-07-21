from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views.generic.edit import CreateView
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import User, Listings, Bids, Comments



def index(request):
    if request.user.id is not None:
        watch = User.objects.get(id=request.user.id)
        return render(request, "auctions/index.html", {
            "Listing": Listings.objects.order_by("-time").filter(status=True), #get only active listings by sorting according to creted date where status is equal to True
            "title": "Active Listings",
            "number" : watch.watch.count()
        })
    else:
        return render(request, "auctions/index.html", {
            "Listing": Listings.objects.order_by("-time").filter(status=True), #get only active listings by sorting according to creted date where status is equal to True
            "title": "Active Listings"
        })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password is not empty
        password = request.POST["password"]
        if password == "":
            return render(request, "auctions/register.html", {
                "message": "Password must not be empty."
            })

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def categories(request):
    return render(request, "auctions/index.html")

# watchlist page view function
def watchlist(request):
    user = User.objects.get(id=request.user.id)
    return render(request, "auctions/index.html", {
        "Listing": Listings.objects.order_by("-time").filter(watchlist=user, status=True),
        "title": "Watchlist",
        "number" : user.watch.count(),
    })

#create listings
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        startingprice = request.POST["startingprice"]
        link = request.POST["link"]
        category = request.POST["category"]
        user = User.objects.get(id=request.user.id)
        if title == "" or description == "" or startingprice == "":  #if manadatory fields not entered then return message
            return render(request, "auctions/create.html", {
                "message": "Enter Mandatory fields",
                "number": user.watch.count()
            })
        else:   #if manadatory fields entered then save
            listing = Listings.objects.create(title=title, description=description, startingprice=startingprice, link=link, category=category, listedby=user)
            listing.save()  
            return index(request)
    else:
        user = User.objects.get(id=request.user.id)
        return render(request, "auctions/create.html", {
            "number": user.watch.count()
        })

# listing details page view function
@login_required(login_url='login')
def listing_page(request, id):
    page = Listings.objects.get(id=id)
    watch = User.objects.get(id=request.user.id)
    return render(request, "auctions/listings.html", {
        "name": page.title,
        "url": page.link,
        "description": page.description,
        "price": page.startingprice,
        "created": page.listedby,
        "category": page.category.title,
        "watchlist": page.watchlist.filter(id=request.user.id).exists(),
        "number": watch.watch.count(),
        "id": page.id
    })

# adds listing to users watchlist
def add_watch(request, id):
    list = Listings.objects.get(id=id)
    user = [User.objects.get(id=request.user.id)]
    list.watchlist.set(user)
    return listing_page(request, id)

# removes listing to users watchlist
def remove_watch(request, id):
    list = Listings.objects.get(id=id)
    user = User.objects.get(id=request.user.id)
    list.watchlist.remove(user)
    return listing_page(request, id)

# placing bid
def bid(request):
    bid = request.POST['bidprice']
    id = request.POST['ID']
    list = Listings.objects.get(id=id)
    user = [User.objects.get(id=request.user.id)]
    if float(bid) > float(list.startingprice):
        #list.bidprice = float(bid)
        #list.save()
        return listing_page(request, id)
    else:
        print("Your bid must be higher than current price")