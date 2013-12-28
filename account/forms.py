from datetime import datetime
from django import forms
from .models import Education

YEAR_CHOICES = [i for i in xrange(1900, datetime.now().year)]


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ['school', 'start_year', 'end_year', 'degree']
        widgets = {
            #'start_year': forms.TextInput(attrs={'placeholder': '2005'}),
            #'end_year': forms.TextInput(attrs={'placeholder': '2009'}),
            'start_year': forms.ChoiceField(choices=YEAR_CHOICES),
            'end_year': forms.ChoiceField(choices=YEAR_CHOICES),
        }

    def clean_end_year(self):
        try:
            start_year = self.cleaned_data['start_year']
        except KeyError:
            raise forms.ValidationError('End Year must be after Start Year')
        try:
            end_year = self.cleaned_data['end_year']
        except KeyError:
            raise forms.ValidationError('End Year must be after Start Year')
        if start_year > end_year:
            raise forms.ValidationError('End Year must be after Start Year')
        return end_year
