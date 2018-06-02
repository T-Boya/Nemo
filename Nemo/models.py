from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Set(models.Model):
    title = models.CharField()

class T1(models.Model):
    textA = models.CharField()
    Set = models.ForeignKey(Set)

class SetForm(forms.ModelForm):
    title = forms.CharField(required=True)
    textA_0 = forms.CharField(required=True)
    textA_1 = forms.CharField(required=True)
    textA_2 = forms.CharField(required=True)
    textB_0 = forms.CharField(required=True)
    textB_1 = forms.CharField(required=True)
    textB_2 = forms.CharField(required=True)

    class Meta:
        model = Profile

    def save(self):
        Set = self.instance
        Set.title = self.cleaned_data[title]

        Set.textA_set.all().delete()
        For i in range(3):
           textA = self.cleaned_data[“textA_{}”.format(i]
           Set.objects.create(
               title=title, interest=interest)
