from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ('-pub_date')
    def _str_(self):
        return self.title     

# Create your models here.
