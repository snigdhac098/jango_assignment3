from django.db import models


class Category(models.Model):
    Category_name = models.CharField(max_length=255, unique=True)
    # tasks = models.ManyToManyField(Task, blank=True)

   
    def __str__(self):  
        return self.Category_name