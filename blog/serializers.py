from rest_framework import serializers
from blog.models import Post
from account.serializers import BaseUserSerializer


class PostListSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer()
    created = serializers.DateTimeField(source='get_created_at')
    updated = serializers.DateTimeField(source='get_updated_at')
    category = serializers.SerializerMethodField(method_name='get_category')

    def get_category(self, obj):
        context = {
            'category': obj.category.title,
            'sub_category': obj.category.sub_category
        }
        return context

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'category', 'thumbnail_image', 'thumbnail_alt', 'status',
                  'created', 'updated', "meta_title", "meta_description", "canonical_check", "canonical_url",
                  "schema_json"]


class PostDetailSerializer(PostListSerializer):
    tag = serializers.SerializerMethodField()

    def get_tag(self, obj):
        if obj.tag is not None:
            context = {
                'tag': obj.tag.title,
                'sub_tag': obj.tag.sub_tag
            }
            return context
        return None

    class Meta:
        model = Post
        fields = ['content', 'tag'] + PostListSerializer.Meta.fields
