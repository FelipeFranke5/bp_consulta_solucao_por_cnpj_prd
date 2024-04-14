from automador_auxiliar import AutomadorBuscaCNPJ


def obter_listagem_cnpj():
    automador = AutomadorBuscaCNPJ()
    return automador.obter_dicionario_cnpjs()
