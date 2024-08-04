from django.db import models
from post.models import POST
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(POST, on_delete=models.CASCADE)
    body = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.body
