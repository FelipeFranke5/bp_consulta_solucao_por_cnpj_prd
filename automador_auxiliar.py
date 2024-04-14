class AutomadorGerenciadorArquivo:

    def __init__(self):
        self.linhas = self.obter_linhas()

    def obter_linhas(self):
        with open('1.txt', encoding='utf-8') as arquivo:
            return arquivo.read().splitlines()


class AutomadorBuscaCNPJ:

    def __init__(self):
        gerenciador_arquivo = AutomadorGerenciadorArquivo()
        self.linhas = gerenciador_arquivo.linhas

    def formatar_cnpj(self, cnpj: str):
        return '{}.{}.{}/{}-{}'.format(
            cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:],
        )

    def obter_dicionario_cnpjs(self):
        dados: dict[str, list[str | None]] = {}

        for linha in self.linhas:
            linha.strip()
            if linha.startswith('DOC'):
                cnpj = linha.split()[1]
                cnpj = self.formatar_cnpj(cnpj)
                dados[cnpj] = []

            if linha and len(linha) == 10:
                dados[cnpj].append(linha)

            if linha == 'NONE':
                dados[cnpj] = []

        return dados
