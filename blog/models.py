from django.db import models

# Create your models here.
# テーブルを作成するファイル

# クラスを定義してその中で変数を定義するだけでテーブルを作成できる。
class Post(models.Model):
    title = models.CharField(max_length=100) #文字数指定必要
    content = models.TextField()             #文字数指定不要
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return self.title