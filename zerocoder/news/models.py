from django.db import models

class News_post(models.Model):
	title = models.CharField('Название новости', null=True, max_length=50)
	short_description = models.CharField('Краткое описание новости', null=True, max_length=200)
	text = models.TextField('Новость', null=True)
	autor = models.TextField('Автор статьи', null=True)
	pub_date = models.DateTimeField('Дата публикации', null=True)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
