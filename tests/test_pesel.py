import pytest
from datetime import date
from pesel_validator.views import PESELValidator

@pytest.mark.parametrize("pesel,valid", [
    ("44051401359", True), # poprawny
    ("92071512346", True), # poprawny
    ("85030812353", True), # poprawny
    ("22222222222", False), # sztuczny
    ("11111111111", False), # sztuczny
    ("00000000000", False), # sztuczny
    ("12345678901", False), # niepoprawny
    ("8503081234", False),  # za krótki
    ("850308123471", False),# za długi
    ("8503081234A", False), # litera
])
def test_validate_checksum_and_length(pesel, valid):
    result = PESELValidator.validate_pesel(pesel)
    assert result["is_valid"] is valid


def test_gender_extraction():
    assert PESELValidator._extract_gender("44051401359") == "Mężczyzna"
    assert PESELValidator._extract_gender("92071512348") == "Kobieta"


def test_birth_date_extraction():
    assert PESELValidator._extract_birth_date("85030812347") == date(1985,3,8)
    assert PESELValidator._extract_birth_date("03261098765") == date(2003,6,10)


def test_age_non_negative():
    res = PESELValidator.validate_pesel("44051401359")
    assert res["is_valid"]
    assert res["age"] >= 0
