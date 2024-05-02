from django.db import models

TITLE_MAX_LEN = 32
CONTENT_MAX_LEN = 576

class Paragraph(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LEN)
    text_content = models.CharField(max_length=CONTENT_MAX_LEN)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def like(self):
        self.upvote += 1

    def dislike(self):
        self.downvote += 1

    def __str__(self):
        return f"TITLE: {self.title}, TEXT CONTENT: {self.text_content}"

# Possible feature, don't implement it yet
# class Comment(models.Model):
#     pass
