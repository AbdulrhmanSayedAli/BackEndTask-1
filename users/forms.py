from django import forms
from django.core.exceptions import ValidationError
import re


def PasswordValidator(password):
    if re.search("[0-9]", password) == None:
        raise ValidationError(
            "Password should contain at least 1 number", code="num_in_Pass")

    if re.search("[A-Z]", password) == None:
        raise ValidationError(
            "Password should contain at least 1 capital letter", code="capLetter_in_Pass")

    return password


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, max_length=20, validators=[PasswordValidator])
    birthDate = forms.DateField()

    def unRequireAll(self):
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False
        self.fields["email"].required = False
        self.fields["password"].required = False
        self.fields["birthDate"].required = False
