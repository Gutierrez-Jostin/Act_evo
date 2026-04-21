from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Books(models.Model):

    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICE_STATUS = {
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    }
    
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.CharField(max_length=2000)
    created_at =models.CharField(auto_now_add=True)
    update_at = models.CharField(auto_now=True)

    def __str__(self):
        return self.title