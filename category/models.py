from django import models
from django.contrib.auth.models import User


class Category(models.Model):
    CATEGORY_CHOICES = (
        ("P", "Pending for Approval"),
        ("R", "Rejected"),
        ("A", "Approved"),
        ("B", "Blocked"),
    )
    name = models.CharField("Category Name", max_length=24, unique=True)
    description = models.TextField(
        "Category Description", max_length=500, null=True, blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created On")
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Created By"
    )
    updated_on = models.DateTimeField("Last Updated On", auto_now=True)
    status = models.CharField(
        "Category Status", max_length=1, choices=CATEGORY_CHOICES, default="P"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
