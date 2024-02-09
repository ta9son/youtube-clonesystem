from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid


def load_path_video(instance, filename):
    return '/'.join(['video', str(instance.title)+str('.mp4')])

def load_path_thum(instance, filename):

    ext = filename.split('.')[-1]
    return '/'.join(['thum', str(instance.title)+str(".")+str(ext)])


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  # 修正: emailを正規化し、extra_fieldsを適用
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    


class User(AbstractBaseUser,PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True,
                          editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    # related_nameを追加して、逆参照時の名前の衝突を解決
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_permissions",
        related_query_name="user",
    )

    def __str__(self):
        return self.email
    


class Video(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True,
                          editable=False)
    title = models.CharField(max_length=30, blank=False)
    video = models.FileField(blank=False, upload_to=load_path_video)
    thum = models.ImageField(blank=False, upload_to=load_path_thum)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    





