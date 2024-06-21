from django import forms

from User.models import UserRegister_Model


class UserRegister_Form(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserRegister_Model
        fields = ('name','email','username','password', 'phoneno', 'gender')
