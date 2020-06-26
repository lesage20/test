from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    """ article section """
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='articles-images')
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        return self.title


class Comment(models.Model):


    commentator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentator')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments_article')
    message = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.commentator_name
    