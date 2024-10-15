from allauth.account.forms import SignupForm
from django_countries.fields import CountryField
from django import forms


class CustomSignUpForm(SignupForm):
    location = CountryField().formfield(required=True,label="Country")
    age = forms.IntegerField()

    def save(self,request):
        user = super(CustomSignUpForm,self).save(request)
        user.save()
        return user
