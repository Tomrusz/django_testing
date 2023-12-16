from django.test import TestCase
from .models import Article, Author
from django.core.files.uploadedfile import SimpleUploadedFile


class ArticleTestCase(TestCase):

    testContent="""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                Nunc vitae nulla quis massa gravida pulvinar. 
                Nulla sed nunc volutpat, feugiat tortor non, lacinia lacus. Vivamus mi ligula, 
                luctus nec consectetur sit amet, rhoncus sed mi. Phasellus tincidunt sed sapien eu feugiat. 
                Quisque in lectus sit amet nisi dictum mollis. Suspendisse potenti. Donec egestas felis nibh, 
                eget commodo mi venenatis eu. Maecenas faucibus ex neque, ac cursus purus fermentum eget.
                """
    def setUp(self):
        author = Author.objects.create(name="Test Author", age=18)
        Article.objects.create(
            title="Test",
            content=self.testContent,
            year=2023,
            author=author,
            is_published=True,
            imgThumb=SimpleUploadedFile(
                name='test_image.jpg',
                content=b"file_content",
                content_type='image/jpeg'
            )
        )

    def tearDown(self):
        article = Article.objects.get(title="Test")
        article.imgThumb.delete()

    def test_article_author(self):
        article = Article.objects.get(title="Test")
        self.assertEqual(article.author.name, "Test Author")

    def test_article_published_status(self):
        article = Article.objects.get(title="Test")
        self.assertTrue(article.is_published)

    def test_article_published_date(self):
        article = Article.objects.get(title="Test")
        self.assertIsNotNone(article.published_date)

    def test_article_last_updated(self):
        article = Article.objects.get(title="Test")
        self.assertIsNotNone(article.last_updated)

    def test_calculate_content_length(self):
        article = Article.objects.get(title="Test")
        expected_length = len(self.testContent)
        self.assertEqual(article.calculate_content_length(), expected_length)

    def test_short_content(self):
        article = Article.objects.get(title="Test")
        self.assertTrue(len(article.short_content) <= 53)

    def test_img_thumb(self):
        article = Article.objects.get(title="Test")
        self.assertIsInstance(article.imgThumb, article.imgThumb.field.attr_class)
