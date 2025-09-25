from django.shortcuts import render
from .forms import PESELForm
from datetime import datetime, date

class PESELValidator:
    """
    Class for validating Polish PESEL numbers according to official specification.
    """

    @staticmethod
    def validate_pesel(pesel):
        """
        Validates PESEL number and extracts information.
        Returns dict with validation result and extracted data.
        """
        if len(pesel) != 11 or not pesel.isdigit():
            return {
                'is_valid': False,
                'error': 'PESEL musi składać się z dokładnie 11 cyfr'
            }

        # Heurystyka: odrzuć PESEL składający się z jednakowych cyfr (np. 111..., 222..., 000...)
        if len(set(pesel)) == 1:
            return {
                'is_valid': False,
                'error': 'Numer PESEL nie może składać się wyłącznie z jednakowych cyfr'
            }

        # Extract date and gender info
        try:
            birth_date = PESELValidator._extract_birth_date(pesel)
            gender = PESELValidator._extract_gender(pesel)

            # Validate checksum
            if not PESELValidator._validate_checksum(pesel):
                return {
                    'is_valid': False,
                    'error': 'Nieprawidłowa suma kontrolna PESEL'
                }

            return {
                'is_valid': True,
                'birth_date': birth_date,
                'gender': gender,
                'age': PESELValidator._calculate_age(birth_date)
            }

        except ValueError as e:
            return {
                'is_valid': False,
                'error': str(e)
            }

    @staticmethod
    def _extract_birth_date(pesel):
        """Extract birth date from PESEL."""
        year = int(pesel[0:2])
        month = int(pesel[2:4])
        day = int(pesel[4:6])

        # Determine century based on month encoding
        if month >= 1 and month <= 12:
            # 1900-1999
            year += 1900
        elif month >= 21 and month <= 32:
            # 2000-2099
            year += 2000
            month -= 20
        elif month >= 41 and month <= 52:
            # 2100-2199
            year += 2100
            month -= 40
        elif month >= 61 and month <= 72:
            # 2200-2299
            year += 2200
            month -= 60
        elif month >= 81 and month <= 92:
            # 1800-1899
            year += 1800
            month -= 80
        else:
            raise ValueError('Nieprawidłowy miesiąc w numerze PESEL')

        # Additional validation - month must be 1-12 after decoding
        if month < 1 or month > 12:
            raise ValueError('Nieprawidłowy miesiąc w numerze PESEL')

        # Additional validation - day must be reasonable
        if day < 1 or day > 31:
            raise ValueError('Nieprawidłowy dzień w numerze PESEL')

        try:
            return date(year, month, day)
        except ValueError:
            raise ValueError('Nieprawidłowa data urodzenia w numerze PESEL')

    @staticmethod
    def _extract_gender(pesel):
        """Extract gender from PESEL."""
        gender_digit = int(pesel[9])
        return 'Mężczyzna' if gender_digit % 2 == 1 else 'Kobieta'

    @staticmethod
    def _validate_checksum(pesel):
        """Validate PESEL checksum."""
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

        sum_weighted = sum(int(pesel[i]) * weights[i] for i in range(10))

        control_digit = (10 - (sum_weighted % 10)) % 10

        return control_digit == int(pesel[10])

    @staticmethod
    def _calculate_age(birth_date):
        """Calculate age based on birth date."""
        today = date.today()
        age = today.year - birth_date.year

        # Adjust if birthday hasn't occurred this year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1

        return age

def validate_pesel(request):
    result = None

    if request.method == 'POST':
        form = PESELForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel']
            result = PESELValidator.validate_pesel(pesel)
            result['pesel'] = pesel
    else:
        form = PESELForm()

    return render(request, 'pesel_validator/validate.html', {
        'form': form,
        'result': result
    })
