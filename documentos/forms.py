from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from documentos.validation import *

from documentos.models import Registro

class RegistroForms(forms.ModelForm):
    data_pesquisa = forms.DateField(
        label='Data de pesquisa',
        disabled=True,
        initial=datetime.today
    )

    class Meta:
        model = Registro
        fields = '__all__'
        labels = {'nome': 'Nome', 'email': 'Email', 'data_nascimento': 'Data de nascimento', 'cpf': 'CPF', 'cep': 'CEP', 'celular': 'Celular'}

        widgets = {
            'data_nascimento': DatePicker(
                options={
                    'minDate': '2009-01-20',
                    'maxDate': '2017-01-20',
            },
            )
        }


    def clean(self):
        nome = self.cleaned_data.get('nome')
        email = self.cleaned_data.get('email')
        cpf = self.cleaned_data.get('cpf')
        cep = self.cleaned_data.get('cep')
        celular = self.cleaned_data.get('celular')

        lista_erros = {}

        campo_com_numero(nome, 'nome', lista_erros)

        valida_cpf(cpf, 'cpf', lista_erros)
        valida_cep(cep, 'cep', lista_erros)

        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_error = lista_erros[erro]
                self.add_error(erro, mensagem_error)

        return self.cleaned_data


