# Comando de Análise de Arquivos Fasta

Este comando realiza a análise de um arquivo Fasta enviado ao bot e retorna informações organizadas, como a sequência, seu ID, tamanho, complemento, template e RNA. Ele utiliza a biblioteca BioPython e discord.py para realizar a análise e interagir com o ambiente do Discord.

## Comando de Análise de Arquivos Fasta

Esse comando permite a análise de arquivos Fasta enviados ao bot. Ele itera sobre as sequências presentes no arquivo Fasta e extrai informações como ID, sequência, tamanho, complemento, template e RNA. Em seguida, as informações são organizadas e escritas em um arquivo de texto que é enviado de volta ao usuário.

### Funções Utilizadas

- **upload**: Essa função é decorada com `@commands.command("UploadFasta")` e representa o comando propriamente dito. Ela recebe o contexto (`ctx`) e o arquivo Fasta como um objeto `discord.Attachment`. Em seguida, lê o conteúdo do arquivo, realiza a análise da sequência e suas informações usando a biblioteca BioPython, organiza as informações e as escreve em um arquivo de texto. Por fim, envia o arquivo de texto de volta ao usuário.

### Utilização

Para utilizar o comando, envie um arquivo Fasta como anexo em uma mensagem no Discord com o comando `UploadFasta`. O bot realizará a análise do arquivo e enviará as informações organizadas em um arquivo de texto de volta ao usuário.


## Tradução de proteinas
Caso  esteja procurando como realizar a tradução de um arquivo contendo uma sequencia de DNA - por exeplo, procure pela pasta *'tradutiontable'*