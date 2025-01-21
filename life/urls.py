from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('game/', views.game, name='game'),
    path('update/', views.update_grid, name='update'),
    path('new/', views.new_grid, name='new'),
]