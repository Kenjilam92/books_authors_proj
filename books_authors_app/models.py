from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    desc= models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f'{self.title}'

class Author(models.Model):
    first_name= models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    book= models.ManyToManyField(Book, related_name="author")
    notes= models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f'{self.first_name}'



# Create your models here.
