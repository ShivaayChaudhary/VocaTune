from django.shortcuts import render
from .forms import AudioForm
from .ml_model.predict_accent import predict_accent

def home(request):
    result = None
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            result = predict_accent(file.audio.path)
    else:
        form = AudioForm()
    return render(request, 'home.html', {'form': form, 'result': result})
