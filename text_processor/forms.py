from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(
        label='Wybierz plik tekstowy',
        help_text='Dozwolone formaty: .txt',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.txt,text/plain'
        })
    )

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith('.txt'):
                raise forms.ValidationError('Dozwolone są tylko pliki .txt')
            if file.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError('Plik nie może być większy niż 5MB')
        return file
