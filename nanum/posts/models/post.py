from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models

from . import PostManager

__all__ = (
    'Question',
    'Answer',
)


# user가 None이면 쿼리에서 제외
class QuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(user=None)


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=150)
    topics = models.ManyToManyField('topics.Topic', related_name='questions')
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = QuestionManager()

    def save(self, *args, **kwargs):
        super().save()
        PostManager.objects.get_or_create(question=self)


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    content = JSONField(blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save()
        post_manager = PostManager.objects.get_or_create(answer=self)

class AnswerImage(models.Model):
    image = models.ImageField(null=False)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='answer_image_set')