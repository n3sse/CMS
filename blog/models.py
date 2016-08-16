from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=128)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Authors"
        ordering = ['-nick']

    def __str__(self):
        return u'%s' % self.nick


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(Author)
    tags = models.CharField(max_length=128)
    published_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['published_date']

    def __str__(self):
        return u'%s %s %s' % (self.title, ' - posted by ', self.author)

    def content_length(self):
        return len(self.content)

