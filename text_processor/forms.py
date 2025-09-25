from django import forms
from django.conf import settings

class FileUploadForm(forms.Form):
    file = forms.FileField(
        label='Wybierz plik tekstowy',
        help_text='Dozwolone formaty: .txt',
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.txt,text/plain',
            'required': False,
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ustaw dynamiczny komunikat z limitem z .env/settings
        max_mb = getattr(settings, 'MAX_UPLOAD_SIZE_MB', 5)
        self.fields['file'].help_text = f'Dozwolone formaty: .txt • Maks. rozmiar: {max_mb} MB'

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            raise forms.ValidationError('Proszę wybrać plik (format .txt)')
        if file:
            if not file.name.lower().endswith('.txt'):
                raise forms.ValidationError('Dozwolone są tylko pliki .txt')
            # Opcjonalna walidacja typu MIME (może zależeć od przeglądarki/systemu)
            content_type = getattr(file, 'content_type', '') or ''
            if content_type and content_type not in ('text/plain', 'application/octet-stream'):
                raise forms.ValidationError('Nieprawidłowy typ pliku. Wgraj plik tekstowy (.txt)')
            # Limit rozmiaru z settings (.env)
            max_bytes = getattr(settings, 'MAX_UPLOAD_SIZE_BYTES', 5 * 1024 * 1024)
            if file.size > max_bytes:
                max_mb = getattr(settings, 'MAX_UPLOAD_SIZE_MB', 5)
                raise forms.ValidationError(f'Plik nie może być większy niż {max_mb} MB')
        return file
