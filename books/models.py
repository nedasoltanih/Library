from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    birthplace = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=200)
    edition = models.IntegerField()
    genre = models.CharField(max_length=3, choices=(('sfi', 'Science Fiction'),('sci','Science'),('fan', 'Fantasy'), ('nov','Novel')))

class Reader(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    books_read = models.ManyToManyField(Book)
