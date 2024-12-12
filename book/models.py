from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to="book_image/")
    description = models.TextField()
    category = models.CharField(max_length=221)
    file = models.FileField(upload_to="book_files/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
