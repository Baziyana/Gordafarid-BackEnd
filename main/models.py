from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_jalali.db import models as jmodels
from ckeditor_uploader import fields
from django.contrib.auth import get_user_model

# ///////////////////////////////// Base Model \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
from blog.util.slug_generetor import unique_slug_generator


class General(models.Model):
    class Meta:
        abstract = True

    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    created_at_gregory = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at_gregory = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    def get_created_at(self):
        return self.created_at.strftime('%H:%M - %Y/%m/%d')

    get_created_at.short_description = 'زمان ایجاد'

    def get_updated_at(self):
        return self.created_at.strftime('%H:%M - %Y/%m/%d')

    get_updated_at.short_description = 'زمان بروزرسانی'


# ///////////////////////////////// Base Category \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class BassCategory(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=350, verbose_name='عنوان')
    description = fields.RichTextUploadingField(verbose_name='توضیحات')
    slug = models.SlugField(unique=True, blank=True, verbose_name='ادرس', allow_unicode=True)
    thumbnail_image = models.ImageField(upload_to='uploads/category/thumbnail_images', verbose_name='تصویر')
    thumbnail_alt = models.CharField(max_length=350, blank=True, verbose_name='عنوان تصویر')
    is_publisher = models.BooleanField(default=False, verbose_name='منتشر شده/نشده')


@receiver(pre_save, sender=BassCategory)
def base_category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = instance.title


# ///////////////////////////////// SEO \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class SEO(models.Model):
    class Meta:
        abstract = True

    meta_title = models.CharField(max_length=350)
    meta_description = models.TextField()
    canonical_check = models.BooleanField(default=False)
    canonical_url = models.URLField(default='')
    schema_json = models.JSONField()


# ///////////////////////////////// Pages \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class Pages(SEO, General):
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='pages', verbose_name='نویسنده')
    title = models.CharField(max_length=350, verbose_name='عنوان')
    content = fields.RichTextUploadingField(verbose_name='توضیحات')
    slug = models.SlugField(unique=True, blank=True, verbose_name='ادرس', allow_unicode=True)
    thumbnail_image = models.ImageField(upload_to='uploads/pages/thumbnail_images', verbose_name='تصویر')
    thumbnail_alt = models.CharField(max_length=350, blank=True, verbose_name='عنوان تصویر')
    is_publisher = models.BooleanField(default=False, verbose_name='منتشر شده/نشده')


@receiver(pre_save, sender=Pages)
def pages_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = instance.title


