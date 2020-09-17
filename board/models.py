from django.db import models


# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    # on_delete = models.CASCADE -> 작성자가 삭제되면 게시글들도 따라서 삭제하겠다
    writer = models.ForeignKey('user.UserInfo', on_delete=models.CASCADE, verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'campus_board'
        verbose_name = '김민혁 커뮤니티 게시글'
        verbose_name_plural = '김민혁 커뮤니티 게시글'
