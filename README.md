# BP - Consulta de Solução (Organizado por CNPJ e EC)

Esse projeto de automação consulta a solução na Braspag e retorna um arquivo
JSON contendo na chave o Número do CNPJ e no valor todos os EC's com suas
respectivas soluções.

## Uso

Automação de uso interno e pessoal.

## Formato do arquivo "1.txt"

O arquivo "1.txt" que contém a lista de CNPJ's deve conter o padrão:


linha 1 - "DOC: {CNPJ}"

linha 2 - "{EC} | NONE"

linha n - "{EC} | NONE"

...


Separar cada bloco com uma linha em branco, por exemplo:


DOC: 00000000000000

0000000000

0000000001

0000000002

... linha em branco ...

DOC: 00000000000001

0000000003

0000000004

0000000005