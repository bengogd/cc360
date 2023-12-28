from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.ai_help_desk, name="ai_chatbot"),
]