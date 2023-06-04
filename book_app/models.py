from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    
    class Meta:
        db_table = 'Book'