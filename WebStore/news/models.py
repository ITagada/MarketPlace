from django.db import models

class articles(models.Model):
    title = models.CharField('Наименование', max_length=50)
    price = models.CharField('Цена', max_length=50)
    description = models.TextField('Описание')
    remains = models.IntegerField('Остаток')

    def __str__(self):
        return f'Товар: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'