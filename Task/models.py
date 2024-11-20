from django.db import models
from Category.models import Category
# Create your models here.





class Task(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Is_completed = models.BooleanField(
        default=False, verbose_name="Is task completed?")
    Assign_date=models.DateField(null=True,blank=True)
    Categories=models.ManyToManyField(Category,blank=True)

    def __str__(self):
        return self.Title
