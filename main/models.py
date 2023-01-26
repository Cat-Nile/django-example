from django.db import models



class Banners(models.Model):
    img=models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text


class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()

