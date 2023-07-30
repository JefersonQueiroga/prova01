from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

# Create your views here.
def cadastro(request):
    return render(request, 'core/form.html')

def lista(request):
    return render(request, 'core/lista.html')

