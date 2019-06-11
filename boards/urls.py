from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # www.mulcam.com/boards/
    path('new/', views.new),  # 사용자의 입력을 받아서 게시글을 작성하는 곳
    path('create/', views.create),  # 사용자가 입력한 데이터를 전송받고 실제 DB에 작성 및 사용자 피드백
    path('<int:id>/', views.detail),  # www.mulcam.com/boards/<id>/
    path('<int:id>/delete/', views.delete),
    path('<int:id>/edit/', views.edit),  # 게시글 수정 페이지 렌더링
    path('<int:id>/update/', views.update),  # 사용자가 입력한 수정 데이터를 전송받고 실제 DB 에 수정 후 저장
]