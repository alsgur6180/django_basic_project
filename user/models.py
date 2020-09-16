from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='가입시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'campus_user'
        verbose_name = '김민혁 커뮤니티 사용자'
        verbose_name_plural = '김민혁 커뮤니티 사용자'
