from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from ..models import Group, Post, User


class PostFormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='auth')

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_create_post(self):
        """Форма создает запись в Post."""
        posts_count = Post.objects.count()
        form_data = {"text": "Текст"}
        response = self.authorized_client.post(
            reverse("posts:post_create"), data=form_data, follow=True
        )
        self.assertRedirects(
            response, reverse(
                "posts:profile", kwargs={"username": self.user.username})
        )
        self.assertEqual(Post.objects.count(), posts_count + 1)
        self.assertTrue(Post.objects.filter(text='Текст').exists())
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_edit(self):
        """Форма изменяет запись в Post."""
        self.post = Post.objects.create(
            author=self.user,
            text='Текст',
        )
        self.group = Group.objects.create(
            title='Тестовая группа',
            slug='slug-test',
            description='Тестовое описание',
        )
        posts_count = Post.objects.count()
        form_data = {'text': "Изменяем текст", 'group': self.group.id}
        response = self.authorized_client.post(
            reverse("posts:post_edit", args=({self.post.id})),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(
            response, reverse(
                "posts:post_detail", kwargs={'post_id': self.post.id})
        )
        self.assertEqual(Post.objects.count(), posts_count)
        self.assertTrue(Post.objects.filter(text='Изменяем текст').exists())
        self.assertEqual(response.status_code, HTTPStatus.OK)
