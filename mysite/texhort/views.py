from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Author, Paragraph, Comment

# Create your views here.

def index(request):
    all_paragraphs = Paragraph.objects.all()
    return render(request, "texhort/index.html", {"paragraphs": all_paragraphs})

def new(request):
    if request.method == "POST":
       # if "text_content" not in request.POST:
       #     error_message = "text content cannot be empty"
       #     return render(request, "texhort/new.html", {"error_message": error_message}) # nah, i'll do it later

       author = Author.objects.get(pk=request.POST["author"])
       text_content = request.POST["text_content"]
       paragraph = Paragraph(text_content=text_content, author=author)
       paragraph.save()
       return redirect(reverse("texhort:index"))

    all_authors = Author.objects.all()
    context = {
        "authors": all_authors
    }
    return render(request, "texhort/new.html", context)

def detail(request, paragraph_id):
    paragraph = get_object_or_404(Paragraph, pk=paragraph_id)
    return render(request, "texhort/detail.html", {"paragraph": paragraph})

def comment(request, paragraph_id):
    paragraph = get_object_or_404(Paragraph, pk=paragraph_id)
    authors = Author.objects.all()
    context = {"paragraph": paragraph, "authors": authors}
    if request.method == "POST":
        if len(request.POST["comment"].strip()) == 0:
            error_message = "comment cannot be empty"
            context["error_message"] = error_message
            return render(request, "texhort/comment.html", context)

        text_content = request.POST["comment"]
        author = get_object_or_404(Author, pk=request.POST["author"])
        comment = Comment(text_content=text_content, author=author, paragraph=paragraph)
        comment.save()
        return redirect(reverse("texhort:detail", args=[paragraph_id]))
    
    return render(request, "texhort/comment.html", context)

def comment_vote(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        if "vote_choice" not in request.POST:
            error_message = "please select like or dislike"
            return render(request, "texhort/comment_vote.html", {"comment": comment, "error_message": error_message})

        if request.POST["vote_choice"] == "upvote":
            comment.like()
        else:
            comment.dislike()

        comment.save()

        return redirect(reverse("texhort:detail", args=[comment.paragraph.id]))
        
    return render(request, "texhort/comment_vote.html", {"comment": comment})

def vote(request, paragraph_id):
    paragraph = get_object_or_404(Paragraph, pk=paragraph_id)
    if request.method == "POST":
        if "vote_choice" not in request.POST:
            error_message = "please select like or dislike"
            return render(request, "texhort/vote.html", {"paragraph": paragraph, "error_message": error_message})

        if request.POST["vote_choice"] == "upvote":
            paragraph.like()
        else:
            paragraph.dislike()

        paragraph.save()

        return redirect(reverse("texhort:index"))
        
    return render(request, "texhort/vote.html", {"paragraph": paragraph})

def author_index(request):
    all_authors = Author.objects.all()
    return render(request, "texhort/author_index.html", {"authors": all_authors})

def author_new(request):
    if request.method == "POST":
        if "username" not in request.POST:
            error_message = "username cannot be empty"
            return render(request, "texhort/author_new.html", {"error_message": error_message})
        
        username = request.POST["username"]    
        author = Author(username=username)
        author.save()
        return redirect(reverse("texhort:author_index"))

    
    return render(request, "texhort/author_new.html")
