from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


    class Meta:
        db_table = "author"

class Ebook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    id_author = models.ForeignKey(Author, on_delete=models.PROTECT)

    class Meta:
        db_table = "book"


