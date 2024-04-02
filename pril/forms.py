from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="введите свое имя")                                           # +-     ,min_length=2, max_length=20
    age = forms.IntegerField(label="Возраст", help_text="введите возраст")
    password = forms.CharField(help_text="введите пароль", widget=forms.PasswordInput)
    required_css_class = 'field'
