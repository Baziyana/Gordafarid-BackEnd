from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.models import Post


class PostTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='user@test.com',
            username='user',
            phone_number='09999999999',
        )
        self.post = Post.objects.create(
            author=self.user,
            title='test title',
            content='test test test',
            status='D'
        )

    def test_str_post_method(self):
        self.assertEqual(str(self.post), 'test title')

    def test_slug_post_model(self):
        self.assertIsNotNone(self.post.slug)
        self.assertEqual(self.post.slug, 'test-title')

    def test_thumbnail_alt_post_model(self):
        self.assertIsNotNone(self.post.thumbnail_alt)
        self.assertEqual(self.post.thumbnail_alt, 'test title')

    def test_author_post_model(self):
        self.assertEqual(self.post.author.email, 'user@test.com')
        self.assertEqual(self.post.author.phone_number, '09999999999')
        self.assertNotEqual(self.post.author.phone_number, '08888888888')

    def test_fields_post_model(self):
        self.assertEqual(self.post.title, 'test title')
        self.assertIsNotNone(self.post.created_at)
        self.assertEqual(self.post.status, "D")

# todo : TestCase Category
# todo : TestCase Tag
