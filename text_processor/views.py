from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FileUploadForm
import random
import re

def scramble_word(word):
    """
    Scrambles letters in the middle of a word, keeping first and last letters in place.
    """
    if len(word) <= 3:
        return word
    
    # Extract first letter, middle letters, and last letter
    first = word[0]
    middle = list(word[1:-1])
    last = word[-1]
    
    # Shuffle middle letters
    random.shuffle(middle)
    
    return first + ''.join(middle) + last

def process_text(text):
    """
    Processes text by scrambling words while preserving punctuation and spacing.
    """
    # Split text into words and non-word characters
    tokens = re.findall(r'\w+|\W+', text)
    
    processed_tokens = []
    for token in tokens:
        if re.match(r'\w+', token):  # If it's a word
            processed_tokens.append(scramble_word(token))
        else:  # If it's punctuation, spaces, etc.
            processed_tokens.append(token)
    
    return ''.join(processed_tokens)

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file = form.cleaned_data['file']
                # Read file content
                content = file.read().decode('utf-8')
                
                # Process the text
                processed_content = process_text(content)
                
                # Store in session for display
                request.session['original_text'] = content
                request.session['processed_text'] = processed_content
                request.session['filename'] = file.name
                
                return redirect('text_processor:result')
                
            except UnicodeDecodeError:
                messages.error(request, 'Nie można odczytać pliku. Upewnij się, że to jest prawidłowy plik tekstowy.')
            except Exception as e:
                messages.error(request, f'Wystąpił błąd podczas przetwarzania pliku: {str(e)}')
    else:
        form = FileUploadForm()
    
    return render(request, 'text_processor/upload.html', {'form': form})

def show_result(request):
    # Get data from session
    processed_text = request.session.get('processed_text')
    original_text = request.session.get('original_text')
    filename = request.session.get('filename')
    
    if not processed_text:
        messages.error(request, 'Brak danych do wyświetlenia. Proszę przesłać plik ponownie.')
        return redirect('text_processor:upload')
    
    context = {
        'processed_text': processed_text,
        'original_text': original_text,
        'filename': filename,
    }
    
    return render(request, 'text_processor/result.html', context)
