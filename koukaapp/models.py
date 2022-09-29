from accounts.models import CustomUser
from django.db import models


class Diary(models.Model):
    """日記モデル"""
    # 必要な項目を列挙する
    # ユーザー：外部キー(カスタムユーザー)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    # タイトル：文字列 最大40文字(max_lengthで最大文字数設定)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    # 本文：テキスト 空白許可(blank=True, null=True)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    # 写真：画像 空白許可(blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    # 作成日時：日付時刻 新規作成時、自動的に現在時刻を設定
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    # 更新日時：日付時刻 更新時、自動的に現在時刻を設定
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = '日記'

    # オブジェクトの文字列表現
    # 管理サイトでの簡易表示用
    def __str__(self):
        return self.title + "(" + self.content[:10] + "...)"