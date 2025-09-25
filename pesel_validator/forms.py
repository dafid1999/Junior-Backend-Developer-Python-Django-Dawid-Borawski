from django import forms
import re

class PESELForm(forms.Form):
    PESEL_LENGTH_ERROR = 'PESEL musi składać się z dokładnie 11 cyfr'
    pesel = forms.CharField(
        label='Numer PESEL',
        help_text='Wprowadź 11-cyfrowy numer PESEL',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg text-center',
            'placeholder': '',
            'maxlength': '11',
            'inputmode': 'numeric'
        }),
        error_messages={
            'required': 'Numer PESEL jest wymagany',
        }
    )

    def clean_pesel(self):
        pesel = self.cleaned_data.get('pesel')

        if not pesel:
            raise forms.ValidationError('Numer PESEL jest wymagany')

        # Remove any whitespace
        pesel = pesel.strip()

        # Check length
        if len(pesel) != 11:
            raise forms.ValidationError(self.PESEL_LENGTH_ERROR)

        # Check if contains only digits
        if not pesel.isdigit():
            raise forms.ValidationError(self.PESEL_LENGTH_ERROR)

        return pesel
