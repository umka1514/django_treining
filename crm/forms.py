from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=200)
    phone = forms.CharField(label='Your phone', max_length=200)
