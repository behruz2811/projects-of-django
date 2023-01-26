from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):  # testcase dan meros oladi
    def setUp(self):
        Post.objects.create(title='Mavzu', text='yangilik matni') #Post dan yangi object yaratyapmiz va yangi post yaratyapmiz
    #test uchun funksiya quyidagicha:
    def test_text_content(self):
        post = Post.objects.get(id=1) #post yaratib uni id sini olyapmiz:
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, 'Mavzu')  # malumotlar bazidan qaytgan mavzu "Mavzu"ga teng bolishi kk...
        self.assertEqual(expected_object_text, 'yangilik matni') # bu ham yuqoridagidek...



# Viewlarni tekshirib chiqish:

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Mavzu 2", text='boshqa yangilik')

    def test_views_url_exist_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
