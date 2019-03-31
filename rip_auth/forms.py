from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RipUser


class RipUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    real_name = forms.CharField(required=True, max_length=20)

    class Meta:
        model = RipUser
        fields = ("email", "real_name", "username", "student_id", "password1", "password2")

    def save(self, commit=True):
        user = super(RipUserCreationForm, self).save(commit=False)

        user.email = self.cleaned_data["email"]
        user.real_name = self.cleaned_data["real_name"]
        user.is_active = True

        if commit:
            user.save()

class RipUserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())


