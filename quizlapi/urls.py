from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('answers', views.AnswerViewSet)
router.register('games', views.GameViewSet)

urlpatterns = [
    path('', include(router.urls)),

]