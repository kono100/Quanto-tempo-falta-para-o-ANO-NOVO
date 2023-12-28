from datetime import timedelta, datetime
import time

print()
print("Contagem Regressiva para o Ano Novo")
print()

try:
    while True:
        data_hoje = datetime.today()
        ano_novo = datetime(year=data_hoje.year + 1, month=1, day=1, hour=0, minute=0, second=0)

        delta_tempo = ano_novo - data_hoje
        relembrar_dias = delta_tempo.days
        relembrar_horas, segundos_restantes = divmod(delta_tempo.seconds, 3600)
        relembrar_minutos, relembrar_segundos = divmod(segundos_restantes, 60)

        mensagem = f'Tempo que falta para o Ano Novo: '

        if relembrar_dias > 0:
            mensagem += f'{relembrar_dias} {"dias" if relembrar_dias > 1 else "dia"} '

        if relembrar_horas > 0:
            mensagem += f'{relembrar_horas} {"horas" if relembrar_horas > 1 else "hora"} '

        if relembrar_minutos > 0:
            mensagem += f'{relembrar_minutos} {"minutos" if relembrar_minutos > 1 else "minuto"} '

        if relembrar_segundos > 0:
            mensagem += f'{relembrar_segundos} {"segundos" if relembrar_segundos > 1 else "segundo"}'

        print(mensagem)

        time.sleep(1)

except KeyboardInterrupt:
    exit()

