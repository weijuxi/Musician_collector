from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('musicians/', views.musicians_index, name='musician-index'),
    path('musicians/<int:musician_id>/', views.musicians_detail, name='musician-detail'),
    path('musicians/create/', views.MusicianCreate.as_view(), name='musician-create'),
    path('musicians/<int:pk>/update/', views.MusicianUpdate.as_view(), name='musician-update'),
    path('musicians/<int:pk>/delete/', views.MusicianDelete.as_view(), name='musician-delete'),
    path('musicians/<int:musician_id>/add_music/', views.add_music, name='add-music'),
]