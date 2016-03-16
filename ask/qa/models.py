#coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Question(models.Model): 
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author', default=1) 
    likes = models.ManyToManyField(User, related_name='question_like', blank=True)
    
    class Meta:
        ordering = ('-added_at',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})

class Answer(models.Model): 
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answer_set') 
    author = models.ForeignKey(User, related_name='au', default=1) 

    class Meta:
        ordering = ('added_at',)

    def __unicode__(self):
        return 'Answer by {}'.format(self.author)
