from django import forms


class CustomerForm(forms.Form):
    """"Класс для валидации формы с сайта"""
    email = forms.EmailField(max_length=50) # проверяем e-mail
    phone = forms.CharField(max_length=15) # проверяем номер телефона
    count_children = forms.IntegerField(max_value=4, min_value=1) # проверяем количество детей
    datetime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M']) # дата и время
