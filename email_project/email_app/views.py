from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import DocumentForm

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'email_app/model_form_upload.html', {
        'form': form
    })


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
