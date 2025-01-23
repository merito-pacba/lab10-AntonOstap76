from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Job(models.Model):
    created_by=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    salary=models.IntegerField()
    location = models.CharField(max_length=100, null=False, blank=False)
    company = models.CharField(max_length=100, null=False, blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-updated', '-posted']

    def __str__(self):
        return self.title


