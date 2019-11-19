from django.db import models
from uuid import uuid4


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400)
    father = models.ForeignKey(
        'self', on_delete=models.CASCADE, to_field='name', blank=True, null=True)

    class Meta:
        ordering = ["name"]


class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    duration = models.DurationField()
    description = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
