from django.db import models

# Create your models here.

class Author(models.Model):
    username = models.CharField(max_length=24)
    joined_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Paragraph(models.Model):
    text_content = models.CharField(max_length=800)
    pub_date = models.DateTimeField(auto_now=True)
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def like(self):
        self.upvote += 1

    def dislike(self):
        self.downvote += 1

    def __str__(self):
        return self.text_content

class Comment(models.Model):
    text_content = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.PositiveIntegerField(default=0)

    def like(self):
        self.upvote += 1

    def dislike(self):
        self.downvote += 1
    
    def __str__(self):
        return self.text_content
