from cpf_cnpj import Documento

# AREA CPF
exemplo_cpf = '11111111111'
documento1 = Documento.cria_documento(exemplo_cpf)
print(documento1)

# AREA CNPJ
exemplo_cnpj = '35379838000112'
documento2 = Documento.cria_documento(exemplo_cnpj)
print(documento2)
