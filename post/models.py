from django.db import models


# Create your models here.
class POST(models.Model):
	POST_CHOICES=(
        ("P", "Pending for Approval"),
        ("R", "Rejected"),
        ("A", "Approved"),
        ("B", "Blocked"),
    	)
	title = models.CharField(max_length=255, error_messages={
		"max_length": 'you cant add more then 250'
		})
	body = models.TextField()
	published_on = models.DateTimeField(auto_now_add=True)
	last_updated_on = models.DateTimeField(auto_now==True)
	slug = models.SlugField(max_length=255, unique=True, blank=True)
	status = models.BooleanField(default='P',choices=POST_CHOICES, max_length=1)


    class Meta:
        verbose_name = "POST"
        verbose_name_plural = "POST"

    def __str__(self):
        return self.title
    