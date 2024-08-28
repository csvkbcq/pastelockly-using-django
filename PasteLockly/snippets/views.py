from django.shortcuts import render, get_object_or_404
from .forms import SnippetForm
from .models import Snippet
from cryptography.fernet import Fernet, InvalidToken
from cryptography.fernet import Fernet

# Generate a valid Fernet key
key = Fernet.generate_key()
print(key.decode())  # This will give you the 32-byte base64 encoded string


def home(request):
    return render(request, 'home.html')

def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            return render(request, 'snippets/view_snippet.html', {'snippet': snippet})
    else:
        form = SnippetForm()
    return render(request, 'snippets/create_snippet.html', {'form': form})

def view_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    decrypted_content = None
    error = None

    if snippet.encrypted:
        if request.method == 'POST':
            key = request.POST.get('key')
            try:
                fernet = Fernet(key.encode())
                decrypted_content = fernet.decrypt(snippet.content.encode()).decode()
            except InvalidToken:
                error = "Invalid decryption key!"
    else:
        decrypted_content = snippet.content

    return render(request, 'snippets/view_snippet.html', {
        'snippet': snippet,
        'decrypted_content': decrypted_content,
        'error': error
    })
