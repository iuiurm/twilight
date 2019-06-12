from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('<int:board_id>/delete/', views.delete, name='delete'),
    path('<int:board_id>/edit/', views.edit, name='edit'),

    # Comments
    path('<int:board_id>/comments/', views.comment_create, name='comment_create'),
]
