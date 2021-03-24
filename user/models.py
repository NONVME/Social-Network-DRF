from django.contrib.auth.models import AbstractUser


class SiteUser(AbstractUser):

    class Meta(object):
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
