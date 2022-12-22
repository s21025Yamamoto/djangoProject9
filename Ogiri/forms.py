from django.forms import ModelForm
from .models import OgiriPost

class OgiriPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''

    class Meta:
        '''ModelFormのインナークラス
        Attribute:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''

        model = OgiriPost
        fields = ['title', 'category']

class ReverseOgiriPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''

    class Meta:
        '''ModelFormのインナークラス
        Attribute:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''

        model = OgiriPost
        fields = ['title', 'category']

class ImageOgiriPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''

    class Meta:
        '''ModelFormのインナークラス
        Attribute:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''

        model = OgiriPost
        fields = ['image', 'category']

class ImitationOgiriPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''

    class Meta:
        '''ModelFormのインナークラス
        Attribute:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''

        model = OgiriPost
        fields = ['title', 'category']





