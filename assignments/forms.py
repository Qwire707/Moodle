from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Напишіть коментар до вашого завдання (необов’язково)'
            }),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            raise forms.ValidationError("Будь ласка, завантажте файл.")
        if file.size > 10 * 1024 * 1024:
            raise forms.ValidationError("Файл не може бути більше 10MB.")
        return file