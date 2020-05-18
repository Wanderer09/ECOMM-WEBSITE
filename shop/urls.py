from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index,name="ShopHome"),
    path("about/", views.about,name="About Us"),
    path("contact/", views.contact,name="Contact Us"),
    path("tracker/", views.tracker,name="TrackingStatus"),
    path("search/", views.search,name="Search"),
    path("products/<int:myid>", views.pView, name="ProductView"),
    path("checkout/", views.checkout ,name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]


