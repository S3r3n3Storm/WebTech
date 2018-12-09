# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import db
from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
        def new():
        	return self.order_by('-added_at')
        def popular():
        	return self.order_by('-rating')

# Create your models here.
class Question(models.Model): #вопрос
	objects = QuestionManager() 
	title = models.CharField(max_length=255) #заголовок вопроса
	text = models.TextField() #полный текст вопроса
	added_at = models.DateTimeField(blank=True, auto_now_add=True) #дата добавления вопроса
	rating = models.IntegerField(default=0) #рейтинг вопроса (число)
	author = models.ForeignKey(User) #автор вопроса (mb link to UserID at User module?)
	likes = models.ManyToManyField(User, related_name='likes_set') #список пользователей, поставивших "лайк" (ManyToMany fields?)
	def __unicode__(self):
		return self.title
	#def get_absolute_url(self):
	#	return '/question/%d/' % self.qk
	class Meta:
		db.table = 'askquestion'
		ordering = ['-added_at']

class Answer(models.Model):
	text = models.TextField() # текст ответа
	added_at = models.DateTimeField(blank=True, auto_now_add=True) # дата добавления ответа
	author = models.ForeignKey(User) # автор ответа
	question = models.ForeignKey(Question) # вопрос, к которому относится ответ
	class Meta:
		db.table = 'answerquestion'
		ordering = ['-added_at']

#question = Question.objects.get(qk=1)
"""
) Рядом с моделью Question определите менеджер реализующий следующие методы

QuestionManager - менеджер модели Question
new - метод возвращающий последние добавленные вопросы
popular - метод возвращающий вопросы отсортированные по рейтингу

6) С помощью команды manage.py syncdb  создайте необходимые таблицы для ваших моделей. Для новых версий django используеются команды makemigrations и migrate."""