from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "post/%s.%s"%(instance.id,extension)

    
    imagename, extension = filename.split('.')
    
    return "post/%s.%s"%(instance.id, extension)

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default= timezone.now)
    image = models.ImageField(upload_to=image_upload)


    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

