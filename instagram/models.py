from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.image.url
    

class HistorySlide(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='history_slides', null=True, blank=True)
    short_text = models.CharField(max_length=50)

    def __str__(self):
        return self.image.url


class History(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    slides = models.ManyToManyField(HistorySlide, related_name='history_slides', null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def add_slide(self, slide):
        self.slides.add(slide)
        self.save()
    
    def remove_slide(self, slide):
        self.slides.remove(slide)
        self.save()
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    instagram_password = models.CharField(max_length=50)
    instagram_username = models.CharField(max_length=50)

    image = models.ImageField(upload_to='characters/')

    def __str__(self):
        return self.name
