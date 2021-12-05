from django.shortcuts import render
from documentos.forms import RegistroForms

# Create your views here.

def index(request):
    form = RegistroForms()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def revisao_validacao(request):
    if request.method == "POST":
        form = RegistroForms(request.POST)
        # Verificando se o formulário está validado.
        if form.is_valid():
            # Passando por contexto os dados resgatados do formulário da página index
            context = {
                'form': form
            }
            return render(request, 'validado.html', context)
        else:
            context = {'form': form}
            return render(request, 'index.html', context)