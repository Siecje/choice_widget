from django.shortcuts import render
from .forms import EducationForm

def education_form(request):
    form = EducationForm()
    return render(request, 'account/education_form.html', {'form': form})

