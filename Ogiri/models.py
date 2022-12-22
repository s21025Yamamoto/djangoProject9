from django.db import models
# accounts　アプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    '''投稿する写真を管理するカテゴリ
    '''

    # カテゴリのフィールド
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        :return: （カテゴリ名）
        '''
        return self.title

class OgiriPost(models.Model):
    """大喜利のお題"""
    # CustomUserモデル（のuser_id)とOgiriPostモデルを
    # １対多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係になる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
    )
    # Categoryモデル（のtitle)とOgiriPostモデルを
    # １対多の関係で結びつける
    # Categoryが親でOgiriPostが子の関係になる
    category = models.ForeignKey(
        Category,
        #　フィールドのタイトル
        verbose_name='カテゴリ',
        #　カテゴリに関連づけられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
    )
    # お題用のフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドの名前
        max_length=200 # 最大文字数は200
    )

    # イメージのフィールド
    image = models.ImageField(
        verbose_name='イメージ',  # フィールドのタイトル
        upload_to='photos'  # MEDIA＿ROOT以下のフォトファイルに保存
    )

    #　投稿日のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True # 日時を自動追加
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        :return:
        '''
        return self.title

class Answer(models.Model):
    """お題に対する回答"""
    # CustomUserモデル（のuser_id)とOgiriPostモデルを
    # １対多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係になる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
    )
    text = models.TextField('お題に対する回答')
    target = models.ForeignKey(OgiriPost, on_delete=models.CASCADE, verbose_name='対象お題')
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',  # フィールドのタイトル
        auto_now_add=True  # 日時を自動追加
    )
    def __str__(self):
        return self.text

class LikeForComment(models.Model):
    """コメントに対するいいね"""
    target = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',  # フィールドのタイトル
        auto_now_add=True  # 日時を自動追加
    )




