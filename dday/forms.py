from django import forms

from .models import Dday


class DdayCreationForm(forms.ModelForm):
    title = forms.CharField(required=True)
    start_date = forms.DateField(localize=True,
                                 widget=forms.DateInput(attrs={'id': 'dday-start-date'}))
    end_date = forms.DateField(localize=True,
                                 widget=forms.DateInput(attrs={'id': 'dday-end-date'}))


    class Meta:
        model = Dday
        fields = ['title', 'start_date', 'end_date']