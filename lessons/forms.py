from django import forms
from .models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file', 'comment']

        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Додатковий коментар...'
            }),
        }