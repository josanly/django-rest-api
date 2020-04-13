from django.db import models

# Create your models here.

class Analysis(models.Model):
    name    = models.CharField(max_length=100, blank=False, default='AA001')
    sample  = models.CharField(max_length=100, blank=False, default='STR_AA001/1/1')
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    class Meta:
        ordering = ['created']