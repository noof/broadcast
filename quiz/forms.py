from django import forms
from .models import Problem, Answer

class ProblemForm(forms.Form):
	text = forms.CharField(max_length=200)
