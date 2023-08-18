from django.db import models

# Create your models here.
class NippoModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 1000)
    timestamp = models.DateTimeField(auto_now_add = True)
    public = models.BooleanField(default = False, verbose_name="公開する")

    def __str__(self):
        return self.title