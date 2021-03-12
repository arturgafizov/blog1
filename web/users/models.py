from django.contrib.auth import get_user_model
from django.db import models

from . import managers
from src.settings import MEDIA_ITEM_IMAGE_DIR

User = get_user_model()


def avatar_upload_patch(obj, filename: str):
    # print(filename.rsplit(".")[-1])
    return f"avatar_images/{obj.user_id}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_set')
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_upload_patch)
    objects = models.Manager()

    def __str__(self) -> str:
        return f'{self.user} {self.id}'

    def save(self, **kwargs):
        return super().save(**kwargs)

    def old_avatar_delete(self):
        if self.avatar:
            self.avatar.delete()
