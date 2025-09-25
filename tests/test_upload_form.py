import io
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from text_processor.forms import FileUploadForm


def make_txt_file(name: str, size_bytes: int) -> SimpleUploadedFile:
    content = (b"A" * size_bytes)
    return SimpleUploadedFile(name=name, content=content, content_type="text/plain")


def test_file_too_large_is_rejected(settings):
    # Ustaw bardzo niski limit rozmiaru, aby łatwo przetestować odrzucenie
    settings.MAX_UPLOAD_SIZE_MB = 1
    settings.MAX_UPLOAD_SIZE_BYTES = 10  # 10 bajtów

    big_file = make_txt_file("test.txt", size_bytes=100)

    form = FileUploadForm(data={}, files={"file": big_file})
    assert not form.is_valid()
    assert "file" in form.errors


def test_file_within_limit_is_accepted(settings):
    settings.MAX_UPLOAD_SIZE_MB = 1
    settings.MAX_UPLOAD_SIZE_BYTES = 1024  # 1 KB

    small_file = make_txt_file("ok.txt", size_bytes=50)

    form = FileUploadForm(data={}, files={"file": small_file})
    assert form.is_valid()
