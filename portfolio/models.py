from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


STATUS_CHOICE = (("Draft", "Draft"), ("Published", "Published"))


class graphics(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='graphics/')
    slug = models.SlugField(unique=True, blank=True)
    status = models.CharField(max_length=10, choices=(('Published', 'Published'), ('Draft', 'Draft')))
    is_featured = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

def generate_unique_slug(instance):
    slug = slugify(instance.title)
    unique_slug = slug
    num = 1
    while graphics.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{num}"
        num += 1
    return unique_slug

@receiver(pre_save, sender=graphics)
def auto_generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)
