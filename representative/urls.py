from django.urls import path
from . import views

urlpatterns = [
    path('gig-csr/', views.gig_csr, name="gig_csr"),
]