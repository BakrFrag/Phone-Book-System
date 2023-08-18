from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    reprsents contact name , contact name unique
    """
    username = models.CharField(max_length=255 , null=False , blank=False)
    def __str__(self):
        return self.username