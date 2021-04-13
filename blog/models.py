#本堂さん、djangoチュートリアル#6参照
from django.db import models
from django.urls import reverse_lazy


# モデルを定義するにはmodels.Modelの継承が必要
class Category(models.Model):
    # カテゴリーには、idと名前が必要のため、nameで名前を作成(idはdjangoが自動で振ってくれるので、何もしなくても良い)
    # 名前は文字で入力されるのでCharFieldが必要
    name = models.CharField(
        max_length=255,
        # 入力しない場合はfalseを返す。入力必須
        blank=False,
        # null(何もない状態)のときはfalseを返す。データベース上の話
        null=False,
        # 他のカテゴリと同じ名前をつけないようにするためにuniqueをTrue
        unique=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    # このモデルを追加したときに自動で日時を追加（新規追加）
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)

    # このモデルを更新したときに自動で日時を追加（新規追加）
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
        
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
        
    body = models.TextField(
        blank=True,
        null=False)
        
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)
    # ManyToManyFieldは一つのブログ記事がタグを複数持てるよということを示す    
    tags = models.ManyToManyField(
        Tag,
        blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])

# Create your models here.
