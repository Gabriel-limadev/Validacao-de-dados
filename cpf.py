from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        """[Classe recebe o número documento ao ser instanciada]

        Args:
            documento ([str]): [Documento cpf deve ser passado]

        Raises:
            ValueError: [Retorna um erro caso o cpf não seja válido]
        """

        documento = str(documento)

        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        """[Descrição do objeto gerado]

        Returns:
            [str]: [Retorna a descrição do objeto]
        """
        return self.format_cpf()

    def cpf_valido(self, cpf):
        """[Valida a quantidade de digitos do cpf e se ele existe]

        Args:
            cpf ([str]): [Número de cpf para ser analisado]

        Raises:
            ValueError: [Retorna um erro caso o cpf não tenha digitos o suficiente]

        Returns:
            [boolean]: [Retorna True caso o cpf exista e False caso contrário]
        """
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválido")

    def format_cpf(self):
        """[Função responsável por criar mascara ao cpf]

        Returns:
            [str]: [Retorna o cpf formatado.]
        """
        mascara = CPF()
        return mascara.mask(self.cpf)
