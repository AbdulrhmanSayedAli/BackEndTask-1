from turtle import title
from django import forms
from django.core.exceptions import ValidationError


def descriptionValidator(desc):
    if len(desc) < 10:
        raise ValidationError(
            "description length should be greater than or equal to 10", code="short_desc")

    if len(desc) > 500:
        raise ValidationError(
            "description length should be smaller than 500", code="long_desc")
    return desc


class CourseForm(forms.Form):

    title = forms.CharField(min_length=5, max_length=20)
    subTitle = forms.CharField(max_length=50)
    description = forms.CharField(validators=[descriptionValidator])
    image = forms.CharField()
    price = forms.FloatField(min_value=0)

    def unRequireAll(self):
        self.fields["title"].required = False
        self.fields["subTitle"].required = False
        self.fields["description"].required = False
        self.fields["image"].required = False
        self.fields["price"].required = False
