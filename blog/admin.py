from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "thumbnail_image", 'get_created_at', "get_updated_at", "status")
    list_editable = ('status',)
    list_filter = ('author', 'status')
    search_fields = ('title',)
