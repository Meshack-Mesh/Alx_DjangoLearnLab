from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostPermissionTests(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username='u1', password='pass')
        self.u2 = User.objects.create_user(username='u2', password='pass')
        self.post = Post.objects.create(title='T', content='C', author=self.u1)

    def test_create_requires_login(self):
        resp = self.client.get(reverse('blog:post_create'))
        self.assertRedirects(resp, f"{reverse('blog:login')}?next={reverse('blog:post_create')}")

    def test_only_author_can_edit(self):
        self.client.login(username='u2', password='pass')
        resp = self.client.get(reverse('blog:post_update', args=[self.post.pk]))
        # logged-in non-author should be redirected or get 403 depending on setup
        self.assertNotEqual(resp.status_code, 200)
