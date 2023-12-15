from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(default='')
    year = models.PositiveIntegerField(default=2023)
    imgThumb = models.ImageField(upload_to='images', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)

    def calculate_content_length(self):
        return len(self.content)

    @property
    def short_content(self):
        if len(self.content) > 50:
            return self.content[:50] + '...'
        return self.content
