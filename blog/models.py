from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver

from django_jalali.db import models as jmodels
from ckeditor_uploader import fields
from django.db.models.signals import post_save, pre_save

from blog.util.slug_generetor import unique_slug_generator


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    created_at_gregory = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at_gregory = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')


class Post(BaseModel):
    class StatusChoices(models.TextChoices):
        Draft = 'D'
        Publish = 'P'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts', verbose_name='نویسنده')
    title = models.CharField(max_length=350, verbose_name='عنوان')
    slug = models.SlugField(unique=True, blank=True, verbose_name='ادرس', allow_unicode=True)
    content = fields.RichTextUploadingField(verbose_name='محتوا')
    thumbnail_image = models.ImageField(upload_to='uploads/posts/thumbnail_images', verbose_name='تصویر')
    thumbnail_alt = models.CharField(max_length=350, blank=True, verbose_name='عنوان تصویر')
    status = models.CharField(max_length=1, choices=StatusChoices.choices, default=StatusChoices.Draft,
                              verbose_name='وضعیت')

    # todo: After writing category model
    # category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts',verbose_name='')

    # todo: After writing tag model
    # tag = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='posts',verbose_name='')

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = instance.title
