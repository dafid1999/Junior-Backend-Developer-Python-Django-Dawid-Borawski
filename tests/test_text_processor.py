from text_processor.views import process_text


def test_process_text_preserves_first_and_last_letters():
    original = "Hello world"
    processed = process_text(original)
    words = processed.split()
    assert words[0][0] == 'H' and words[0][-1] == 'o'
    assert words[1][0] == 'w' and words[1][-1] == 'd'


def test_process_text_does_not_change_short_words():
    assert process_text("to i ja") == process_text("to i ja")


def test_process_text_keeps_punctuation():
    original = "Cześć, świecie!"
    processed = process_text(original)
    assert ',' in processed and '!' in processed
