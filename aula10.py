# Date
# Datetime
# Time
# Timedelta

from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.hour)
    print(data_atual.date())
    print(data_atual.weekday())
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2021, 9, 10, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '10/09/2021 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    #print(data_atual.strftime('%d-%m-%y'))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))

if __name__ == '__main__':
    trabalhando_com_time()
    trabalhando_com_time()
    trabalhando_com_datetime()

