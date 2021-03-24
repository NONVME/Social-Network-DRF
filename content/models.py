from django.db import models
from user.models import SiteUser


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField('Creation date', auto_now_add=True)
    pub_date = models.DateTimeField('Publication date', auto_now=True)
    author = models.ForeignKey(SiteUser,
                               related_name='post_author',
                               on_delete=models.CASCADE)
    evaluator = models.ManyToManyField(SiteUser,
                                       through='PostRate',
                                       related_name='post_evaluator')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.title)


class PostRate(models.Model):
    like = models.BooleanField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} {"Liked" if self.like else "Disliked"} by {self.user}'  # noqa: E501
