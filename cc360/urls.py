from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
	path('personalize/', include('personalize.urls')),
	path('chatbot/', include('chatbot.urls')),
	path('representative/', include('representative.urls')),
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name = "logout"),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)