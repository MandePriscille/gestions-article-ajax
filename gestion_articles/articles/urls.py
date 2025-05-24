from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_article, name='create_article'),
    path('update/<int:id>/', views.update_article, name='update_article'),
    path('delete/<int:id>/', views.delete_article, name='delete_article'),
    path('detail/<int:id>/', views.get_article, name='get_article'),
]