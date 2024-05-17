from django.urls import path

from . import views

app_name = "texhort"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("<int:paragraph_id>/detail/", views.detail, name="detail"),
    path("<int:paragraph_id>/comment/", views.comment, name="comment"),
    path("<int:comment_id>/comment/vote/", views.comment_vote, name="comment_vote"),
    path("<int:paragraph_id>/vote/", views.vote, name="vote"),
    path("author/", views.author_index, name="author_index"),
    path("author/new/", views.author_new, name="author_new"),
]
