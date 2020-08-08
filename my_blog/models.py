from django.db import models
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    text = models.CharField(verbose_name='Текст поста', max_length=500)
    img = models.ImageField(verbose_name='Картинка поста', upload_to='media/')
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])
