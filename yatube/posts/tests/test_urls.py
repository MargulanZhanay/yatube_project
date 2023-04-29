from django.test import TestCase, Client
from ..models import Post, Group
from django.contrib.auth import get_user_model

User = get_user_model()


class PostURLTests(TestCase):
    """Create testing post and group."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='slug-test',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(PostURLTests.user)

    def test_home_url_exists_at_desired_location(self):
        """Page / available to any user."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_group_url_exists_at_desired_location(self):
        """Page /group/<slug>/ available to any user."""
        response = self.guest_client.get(f'/group/{self.group.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_exists_at_desired_location(self):
        """Page /posts/<int:post_id>/ available to any user."""
        response = self.guest_client.get(f'/posts/{self.post.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_profile_url_exists_at_desired_location(self):
        """Page /profile/ available to any user."""
        response = self.guest_client.get(f'/profile/{self.user.username}/')
        self.assertEqual(response.status_code, 200)

    def test_author_post_edit_status_code(self):
        """Page /posts/<int:post_id>/edit/ available to authorized user."""
        response = self.authorized_client.get(f'/posts/{self.post.pk}/edit/')
        self.assertEqual(response.status_code, 200)

    def test_autorized_client_create_post(self):
        """Page /create/ available to authorized user."""
        response = self.authorized_client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_unexisting_page_at_desired_location(self):
        """Page /unexisting_page/ should give an error."""
        response = self.guest_client.get('/unexisting_page/')
        self.assertEqual(response.status_code, 404)
