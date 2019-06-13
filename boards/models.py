from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)  # 해당 필드에 아무것도 안들어가도 된다.
    image = ProcessedImageField(
        upload_to='boards/images',  # 저장위치 (media 이후의 경로)
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 1. 첫번째 포스트
        return f'{self.id}. {self.title}'


class Comment(models.Model):
    content = models.TextField()  # 댓글의 내용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Board({self.board_id}): Comment({self.id} - {self.content})>'
