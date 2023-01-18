from django.db import models

# Create your models here.
class Devtool(models.Model):
    name = models.CharField(max_length=64, blank=True)
    kind = models.CharField(max_length=64, blank=True)
    content = models.CharField(max_length=64, blank=True)
        
class Idea(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(blank=True, upload_to='ideas/%Y%m%d', null=True)
    content = models.TextField()
    interest = models.IntegerField()
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, related_name="idea_devtool")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# class Ideastar(models.Model):
    