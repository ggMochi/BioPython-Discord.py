
# Comandos de Análise de Arquivos GenBank

Este comando realiza a análise de um arquivo GenBank enviado ao bot e retorna informações organizadas, como a sequência, seu ID, tamanho, complemento, template e RNA. Ele utiliza a biblioteca BioPython e discord.py para realizar a análise e interagir com o ambiente do Discord.

## Comando de Análise de Arquivos GenBank

Esse comando permite a análise de arquivos GenBank enviados ao bot. Ele itera sobre as sequências presentes no arquivo GenBank e extrai informações como ID, sequência, tamanho, complemento, template e RNA. Em seguida, as informações são organizadas e escritas em um arquivo de texto que é enviado de volta ao usuário.

### Funções 

- **upload**: Essa função é decorada com `@commands.command("UploadGenbank")` e representa o comando propriamente dito. Ela recebe o contexto (`ctx`) e o arquivo GenBank como um objeto `discord.Attachment`. Em seguida, lê o conteúdo do arquivo, realiza a análise da sequência e suas informações usando a biblioteca BioPython, organiza as informações e as escreve em um arquivo de texto. Por fim, envia o arquivo de texto de volta ao usuário.

### Utilização

Para utilizar o comando, envie um arquivo GenBank como anexo em uma mensagem no Discord com o comando `UploadGenbank`. O bot realizará a análise do arquivo e enviará as informações organizadas em um arquivo de texto de volta ao usuário.


## Comando de Análise de Arquivos GenBank - Anotações de Genoma

Esse comando permite a análise de arquivos GenBank contendo as anotações de um genoma enviados ao bot. Ele itera sobre as features presentes no arquivo GenBank e classifica os genes codificantes, tRNAs e rRNAs encontrados. Em seguida, conta a quantidade de cada tipo de elemento anotado e organiza as informações em um arquivo de texto que é enviado de volta ao usuário.

### Funções Utilizadas

- **uploadProtein**: Essa função é decorada com `@commands.command("UploadGenbankProtein")` e representa o comando propriamente dito. Ela recebe o contexto (`ctx`) e o arquivo GenBank contendo as anotações de um genoma como um objeto `discord.Attachment`. Em seguida, realiza a análise das features presentes no arquivo, contabiliza os genes codificantes, tRNAs e rRNAs e escreve as informações em um arquivo de texto. Por fim, envia o arquivo de texto de volta ao usuário.

### Utilização

Para utilizar o comando, envie um arquivo GenBank contendo as anotações de um genoma como anexo em uma mensagem no Discord com o comando `UploadGenbankGene`. O bot realizará a análise do arquivo e enviará as informações classificadas em um arquivo de texto de volta ao usuário.


## Tradução de proteinas
Caso  esteja procurando como realizar a tradução de um arquivo contendo uma sequencia de DNA - por exeplo, procure pela pasta *'tradutiontable'*