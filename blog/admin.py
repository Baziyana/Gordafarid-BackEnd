from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "thumbnail_image", 'created_at', "updated_at", "status")
    list_editable = ('status',)
    list_filter = ('author', 'status')
    search_fields = ('title',)
