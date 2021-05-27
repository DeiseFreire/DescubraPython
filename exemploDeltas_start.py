#
# Arquivo de exemplos para uso da classe timedeltas
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def QuantosDiasFaltam(ano, mes, dia):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)

    qtosDias = dataProcurada - hoje

    # mensagemRetorno = "Faltam " + str(qtosDias) + "dias para a data " + dataProcurada.str(time("%d/%m/%a"))
    mensagemRetorno = "Faltam " + str(qtosDias).replace("days, 0:00:00", " ") + " dias para a data " + dataProcurada.str(time("%d/%m/%a"))

    print(mensagemRetorno)

QuantosDiasFaltam(2019, 10, 29)