from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import MyLessonViewSet

router = SimpleRouter()
router.register('lessons', MyLessonViewSet, 'lessons')


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]