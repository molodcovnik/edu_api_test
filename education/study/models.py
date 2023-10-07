from django.contrib.auth.models import User
from django.db import models

from catalog.models import Product



class Lesson(models.Model):
    title = models.CharField(max_length=64)
    video_url = models.URLField()
    duration = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.title} {self.video_url} {self.duration}'


class LessonStatusEnum(models.TextChoices):
    VIEWED = 'VIEWED'
    NOT_VIEWED = 'NOT_VIEWED'


class LessonInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='views')
    status = models.CharField(choices=LessonStatusEnum.choices,
                              default=LessonStatusEnum.NOT_VIEWED,
                              max_length=12)
    view_time = models.IntegerField(default=0)

    class Meta:
        unique_together = ('lesson', 'user')

    def __str__(self):
        return f'{self.user} {self.lesson} {self.status} {self.view_time}'