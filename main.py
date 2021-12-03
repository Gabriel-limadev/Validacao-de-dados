import re
from datetime import datetime, timedelta

from cpf_cnpj import Documento
from telefones import Telefones
from datas import Datas
from acesso_cep import BuscaEndereço

# Para utilizar a API
import requests

# AREA CPF
# exemplo_cpf = '50555075869'
# documento1 = Documento.cria_documento(exemplo_cpf)
# print(documento1)

# AREA CNPJ
# exemplo_cnpj = '35379838000112'
# documento2 = Documento.cria_documento(exemplo_cnpj)
# print(documento2)

# AREA TELEFONE - EXPRESSÕES REGULARES
# telefone = "5511957461745"
# telefone_objeto = Telefones(telefone)
# print(telefone_objeto.format_numero())

# AREA DATAS
# cadastro = Datas()

# print(cadastro.tempo_cadastro())

# AREA CEP
cep = '06850150'
objeto_cep = BuscaEndereço(cep)


# API PARA CEP
a = objeto_cep.acessa_via_cep()
print(a)
