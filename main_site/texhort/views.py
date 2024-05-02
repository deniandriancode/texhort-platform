from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Paragraph

def index(request):
    all_paragraphs = get_list_or_404(Paragraph)
    context = {"all_paragraphs": all_paragraphs}
    return render(request, "texhort/index.html", context)

def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        text_content = request.POST["text_content"]
        paragraph = Paragraph(title=title, text_content=text_content)
        paragraph.save()
        return HttpResponseRedirect(reverse("texhort:index"))
    return render(request, "texhort/new.html", {})

def vote(request, paragraph_id):
    paragraph = get_object_or_404(Paragraph, pk=paragraph_id)
    if request.method == "POST":
        if "vote_choice" not in request.POST:
            return render(request, "texhort/vote.html", {"error_message": "Please vote like or dislike.", "paragraph": paragraph})

        if request.POST["vote_choice"] == "upvote":
            paragraph.like()
        else:
            paragraph.dislike()
            
        paragraph.save()
        return HttpResponseRedirect(reverse("texhort:index"))
        
    context = {"paragraph": paragraph}
    return render(request, "texhort/vote.html", context)
