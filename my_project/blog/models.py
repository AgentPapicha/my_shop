from django.db import models
from django.core.files import File

from io import BytesIO
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=400)
    post_text = models.TextField()
    slug = models.SlugField()
    author_name = models.CharField(max_length=100)
    created_at = models.DateField()
    image = models.ImageField(upload_to='uploads/blog_images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/blog_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.slug}"

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail