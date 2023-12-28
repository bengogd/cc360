from django.urls import path
from . import views

urlpatterns = [
    path('ai-recommandations/', views.ai_personalize, name="personalize"),
]