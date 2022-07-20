from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from ckeditor_uploader import fields
from django.db.models.signals import post_save, pre_save
from main.models import General, SEO, Pages, BassCategory
from blog.util.slug_generetor import unique_slug_generator


# /////////////////////////////////////// Post \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class Post(General, SEO):
    class StatusChoices(models.TextChoices):
        Draft = 'D'
        Publish = 'P'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts', verbose_name='نویسنده')
    tag = models.ForeignKey("BlogTag", on_delete=models.CASCADE, related_name='posts', verbose_name='برچسب', null=True)
    category = models.ForeignKey("BlogCategory", on_delete=models.CASCADE, related_name='posts',
                                 verbose_name='دسته بندی', null=True)

    title = models.CharField(max_length=350, verbose_name='عنوان')
    slug = models.SlugField(unique=True, blank=True, verbose_name='ادرس', allow_unicode=True)
    content = fields.RichTextUploadingField(verbose_name='محتوا')
    thumbnail_image = models.ImageField(upload_to='uploads/posts/thumbnail_images', verbose_name='تصویر')
    thumbnail_alt = models.CharField(max_length=350, blank=True, verbose_name='عنوان تصویر')
    status = models.CharField(max_length=1, choices=StatusChoices.choices, default=StatusChoices.Draft,
                              verbose_name='وضعیت')

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = instance.title


# /////////////////////////////////////// Post Tag \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class BlogTag(General, BassCategory, SEO):
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    tag = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='tags', verbose_name='برچسب')


# /////////////////////////////////////// Post Category \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class BlogCategory(General, BassCategory, SEO):
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    category = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='categories',
                                 verbose_name='دسته بندی')


# /////////////////////////////////////// Post Comment \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class BlogComment(models.Model):
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
