from django.db import models
from django.urls import reverse

class SiteMenu(models.Model):

    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    def __str__(self):
        return self.title
    

    