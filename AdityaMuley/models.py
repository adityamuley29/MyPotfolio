from django.db import models

# Create your models here.

class Projects(models.Model):

    project_img = models.ImageField()
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    source_code = models.URLField()

    def __str__(self):
        return self.title


class Contact(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name