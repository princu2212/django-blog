from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, default='Sample')
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    document = models.FileField(upload_to='uploads/', default='')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title