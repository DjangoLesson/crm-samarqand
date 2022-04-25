from django.contrib.auth.models import AbstractUser
# from ckeditor.fields import RichTextField

from .managers import UserManager

# content = RichTextField(config_name='awesome_ckeditor')

class User(AbstractUser):
    objects: UserManager = UserManager()

    def __str__(self):
        return self.email