from django.shortcuts import render
from .models import Board


# Create your views here
def index(request):
    # Board 의 전체 데이터를 불러온다 - QuerySet
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


# 사용자 입력을 받는 페이지 렌더링
def new(request):
    return render(request, 'boards/new.html')


# 데이터를 받아서 실제 DB 에 작성
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    board = Board(title=title, content=content)
    board.save()
    return render(request, 'boards/create.html')
