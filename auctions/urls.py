from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addlisting", views.addlisting, name="addlisting"),
    path("visitlisting/<int:listid>", views.visitlisting, name="visitlisting"),
    path("addcomment", views.addcomment, name="addcomment"),
    path("addbid", views.addbid, name="addbid"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("wonlisting", views.wonlisting, name="wonlisting"),
    path("categories", views.categories, name="categories"),
    path("endbid/<int:listid>", views.endbid, name="endbid"),
    path("displaycategories/<str:category>",
         views.displaycategories, name="displaycategories"),
    path("work", views.work, name="work")

]
