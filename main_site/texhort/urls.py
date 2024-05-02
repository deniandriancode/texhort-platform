from django.urls import path

from . import views

app_name = "texhort"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("<int:paragraph_id>/vote/", views.vote, name="vote"),
]
