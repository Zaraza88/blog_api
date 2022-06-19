from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField('название поста', max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(MPTTModel):
    email = models.EmailField()
    text = models.TextField('Сообщение', max_length=5000)
    parent = TreeForeignKey(
        'self', verbose_name='Родитель', 
        on_delete=models.SET_NULL, blank=True, null=True,
        related_name='children'
    )
    post = models.ForeignKey(
        Post, verbose_name='пост', 
        on_delete=models.CASCADE, 
        related_name='post_comment'
    )
    name = models.ForeignKey(
        User, blank=True, null=True, 
        on_delete=models.PROTECT, verbose_name='Автор комментария',
        related_name='comment_name'
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.post} - {self.id}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Like(models.Model):
    CHOICE = (
        ('like', 'like'),
        ('dislike', 'dislike')
    )
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.PROTECT, related_name='likes')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_like')
    like = models.CharField(choices=CHOICE, null=True, blank=True, max_length=7)

    def __str__(self) -> str:
        return f"Пользователь '{self.user}' поставил посту '{self.post}' - {self.like}"

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
