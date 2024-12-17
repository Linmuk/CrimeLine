from django import forms
from .models import CrimeReport

class CrimeReportForm(forms.ModelForm):
    class Meta:
        model = CrimeReport
        fields = ['title', 'description', 'category', 'location','evidence_image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
