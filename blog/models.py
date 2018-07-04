from django.db import models

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128,blank=True,default='')
    title = models.CharField(max_length=128,blank=True,default='')
    body = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "'%s' by %s" % (self.title,self.author)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128,blank=True,default='')
    body = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "%s: %s" % (self.author,self.body)