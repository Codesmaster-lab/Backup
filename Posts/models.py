from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#from storages.backends.ftp import FTPStorage
#fs=FTPStorage()


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=500)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.CharField(max_length=500,blank=True, null=True)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    link=models.URLField(blank=True)
    image=models.ImageField(upload_to='post_pics',blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Codesmaster_Projects_Read',kwargs={'pk':self.pk})


from django.db import models

# Create your models here.
class New(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()

    def __str__(self):
        return self.title
