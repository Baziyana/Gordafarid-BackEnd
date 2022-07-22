from django.contrib import admin
from blog.models import Post,BlogCategory,BlogTag
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "thumbnail_image_tag", 'get_created_at', "get_updated_at", "status", 'tag',
                    'category')
    list_editable = ('status',)
    list_filter = ('author', 'status')
    search_fields = ('title',)

    def thumbnail_image_tag(self, obj):
        return format_html('<img src="{}" style="width: 120px;border-radius: 15px;" />'.format(obj.thumbnail_image.url))

    thumbnail_image_tag.short_description = 'عکس'

admin.site.register(BlogCategory)
admin.site.register(BlogTag)