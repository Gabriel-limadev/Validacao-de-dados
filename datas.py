from datetime import datetime


class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1]

    def dia_semana(self):
        dias_da_semana = [
            'Segunda', 'Terça', 'Quarta',
            'Quinta', 'Sexta', 'Sabádo', 'Domingo'
        ]
        dia_da_semana_cadastro = self.momento_cadastro.weekday()
        print(dia_da_semana_cadastro)
        return dias_da_semana[dia_da_semana_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
