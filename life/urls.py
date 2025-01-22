from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('select/', views.select_pattern, name='select_pattern'),
    path('game/', views.game, name='game'),
    path('update/', views.update_grid, name='update'),
    path('new/', views.new_grid, name='new'),
]