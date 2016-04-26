from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.utils.translation import ugettext as _

from bolt_user.models import BoltUser


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    username = forms.CharField(widget=forms.TextInput, label="User Name")
    email = forms.EmailField(widget=forms.TextInput, label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")
    wordpresslink = forms.CharField(widget=forms.TextInput, label="Wordpress Link")
    wordpressid = forms.CharField(widget=forms.TextInput, label="Wordpress User Name")
    wordpresspass = forms.CharField(widget=forms.PasswordInput, label="Wordpress Password")

    class Meta:
        model = BoltUser
        fields = [
            'username', 'email', 'password1', 'password2',

            # fields for wordpress input
            'wordpress_link', 'wordpress_id', 'wordpress_pass',
        ]

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
