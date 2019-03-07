from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="main"),
    path('new/', views.new, name="card_new"),
    path('create/', views.create, name="create"),
    path('detail/<int:card_id>/', views.detail, name="detail")
]
