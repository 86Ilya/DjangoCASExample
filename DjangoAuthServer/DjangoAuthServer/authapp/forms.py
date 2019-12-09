from django import forms
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator

from DjangoAuthServer.authapp.models import User


username_validator = RegexValidator(r'^[\w\d_\-]+$',
                                    "Username should contain only letters, digits, underscores, and dashes")


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, max_length=120, min_length=3, validators=[username_validator])
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_again')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.fields.get('username', None):
            self.fields['username'].widget.attrs.update({
                'placeholder': 'Username', 'class': 'form-control mb-3'
            })
            self.fields['username'].help_text = ''
            self.fields['username'].label = ''

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email', 'class': 'form-control mb-3'
        })
        self.fields['email'].help_text = ''
        self.fields['email'].label = ''

        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password', 'class': 'form-control mb-3'
        })
        self.fields['password'].help_text = ''
        self.fields['password'].label = ''

        self.fields['password_again'].widget.attrs.update({
            'placeholder': 'Repeat password', 'class': 'form-control mb-3'
        })
        self.fields['password_again'].help_text = ''
        self.fields['password_again'].label = ''

        # this code is for descendants
        # remove unnecessary fields
        unnecessary = set(self.fields.keys()) - set(self.Meta.fields)
        for field in unnecessary:
            self.fields.pop(field)

    def clean(self):
        cleaned_data = super().clean()
        validation_errors = list()
        # Clean password
        password = cleaned_data['password']
        password_again = cleaned_data['password_again']
        if len(password) == 0 and len(password_again) == 0:
            return cleaned_data
        if password != password_again:
            validation_errors.append(forms.ValidationError("Passwords mismatch"))
        elif len(password) < 8:
            validation_errors.append(forms.ValidationError("Password length must be at least 8 symbols"))
        else:
            # TODO is it ok?
            cleaned_data['password'] = make_password(password)

        if validation_errors:
            raise forms.ValidationError(validation_errors)

        return cleaned_data
