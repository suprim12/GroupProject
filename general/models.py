from django.db import models
# Create your models here.


class Slider(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider/')

    def __str__(self):
        return self.caption


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='blog/')
    content = models.TextField()
    cat = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
