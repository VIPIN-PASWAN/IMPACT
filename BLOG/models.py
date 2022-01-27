from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateField(blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title + " by " + self.author
