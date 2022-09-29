import os

from django import forms
from django.core.mail import EmailMessage
from .models import Diary

# お問い合わせ内容を入力するフォーム
class InquiryForm(forms.Form):
    # 入力する内容
    # label：表示する名称
    name = forms.CharField(label='NAME', max_length=30)
    # CharField:<input type='text'>
    email = forms.EmailField(label='MAIL ADDRESS')
    # EmailField:<input type='email'>
    title = forms.CharField(label='TITLE', max_length=30)
    message = forms.CharField(label='MESSAGE', widget=forms.Textarea)
    # 詳細はテキスト.47

    # コンストラクタ
    # 各入力フィールドの属性を設定
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # nameのClass属性にform-controlを設定
        self.fields['name'].widget.attrs['class'] = 'form-control'
        # nameのplaceholder属性に文字列を設定
        self.fields['name'].widget.attrs['placeholder'] = 'input name.'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'input mailaddress.'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'input title.'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'input message.'

    #入力内容を基にメール送信処理を行うメソッド
    def send_email(self):
        # cleaned_dataからエラー処理完了後の入力データを取得
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()

# 日記の内容を入力するフォーム
# ModelForm:モデルへの入力するためのフォーム
class DiaryCreateForm(forms.ModelForm):
    class Meta:
        # 対象モデルを指定
        model = Diary
        # 入力する項目を指定
        fields = ('title', 'content', 'photo1', 'photo2', 'photo3',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for分を使って全項目に同じクラス属性を設定
        # InquiryFormと同じように個別に設定するのがベスト
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'