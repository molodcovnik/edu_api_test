from django.contrib.auth.models import User
from django.db.models import FilteredRelation, Q, F
from rest_framework import generics, mixins, status, viewsets, permissions

from .serializers import MyLessonsSerializer
from catalog.models import Product, ProductAccess
from study.models import Lesson, LessonInfo


class MyLessonViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyLessonsSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        accesses = ProductAccess.objects.filter(user=self.request.user)

        qs = Lesson.objects.filter(
            products__in=accesses.values('product')
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__view_time')
        )
        #     .exclude(
        #     status=None
        # )

        return qs