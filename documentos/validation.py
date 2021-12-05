from validate_docbr import CPF

def campo_com_numero(valor_campo, nome_campo, lista_erros):
    """[Valida se os campos tem números]


    Args:

        valor_campo ([str]): [Valor do campo a ser validado]

        nome_campo ([str]): [Nome do campo a ser validado]

        lista_erros ([dict]): [Lista que contem os erros das validações]
    """

    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Não inclua números nesse campo'

def valida_cpf(valor_campo, nome_campo, lista_erros): 
    documento = CPF()   
    valido = documento.validate(valor_campo)
    if valido:
        pass
    elif len(valor_campo) != 11:
        lista_erros[nome_campo] = 'A quantidade de digitos está incorreta'
    else:
        lista_erros[nome_campo] = 'CPF inválido!'

def valida_cep(valor_campo, nome_campo, lista_erros): 
    if any(not char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Digite apenas número nesse campo'
    elif len(valor_campo) != 8:
        lista_erros[nome_campo] = 'CEP inválido!'


def valida_celular(valor_campo, nome_campo, lista_erros): 
    if any(not char.isnumeric() for char in valor_campo):
        lista_erros[nome_campo] = 'Digite apenas número nesse campo'
    elif len(valor_campo) != 11:
        lista_erros[nome_campo] = 'Quantidade de digitos inválido!'