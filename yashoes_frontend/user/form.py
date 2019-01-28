from django import forms


class UserUpdateForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='phone_number', required=False)
    address = forms.CharField(label='address', required=False)
