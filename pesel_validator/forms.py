from django import forms
import re

class PESELForm(forms.Form):
    pesel = forms.CharField(
        label='Numer PESEL',
        max_length=11,
        min_length=11,
        help_text='Wprowadź 11-cyfrowy numer PESEL',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg text-center',
            'placeholder': '85030812345',
            'pattern': '[0-9]{11}',
            'maxlength': '11'
        })
    )

    def clean_pesel(self):
        pesel = self.cleaned_data.get('pesel')

        if not pesel:
            raise forms.ValidationError('Numer PESEL jest wymagany')

        # Check if contains only digits
        if not re.match(r'^\d{11}$', pesel):
            raise forms.ValidationError('PESEL musi składać się z dokładnie 11 cyfr')

        return pesel
