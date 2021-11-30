import re

# from cpf_cnpj import Documento
from telefones import Telefones

# AREA CPF
# exemplo_cpf = '50555075869'
# documento1 = Documento.cria_documento(exemplo_cpf)
# print(documento1)

# # AREA CNPJ
# exemplo_cnpj = '35379838000112'
# documento2 = Documento.cria_documento(exemplo_cnpj)
# print(documento2)

# AREA TELEFONE - EXPRESSÕES REGULARES
telefone = "5511957461745"
telefone_objeto = Telefones(telefone)
print(telefone_objeto.format_numero())
