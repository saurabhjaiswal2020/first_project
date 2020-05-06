from django import forms
from django.contrib.auth.models import User
from first_app.models import ContactModel, UserProfileInfo

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=50)
    message = forms.CharField(max_length=255)

    class Meta:
        model = ContactModel
        fields = "__all__"



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ("portfolio_site", 'profile_pic')