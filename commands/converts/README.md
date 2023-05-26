# Comandos de conversão de arquivo
Essa pasta contem os comandos necessarios para ser converter arquivos entre diferentes extenções 

### Bibliotecas Utilizadas

- **BioPython**: A biblioteca BioPython é utilizada para lidar com a manipulação e conversão de sequências biológicas. Ela fornece métodos e ferramentas para a leitura, escrita e análise de arquivos GenBank e Fasta, bem como para a conversão entre os formatos.

- **discord.py**: A biblioteca discord.py é uma biblioteca de cliente para interação com a API do Discord. Ela permite a criação de bots personalizados para o Discord e oferece uma interface para lidar com eventos, comandos e interações no ambiente do Discord.

## Comando de Conversão de Arquivos Fasta para GenBank

Este comando permite a conversão de arquivos Fasta enviados ao bot em arquivos GenBank. Ele utiliza as bibliotecas BioPython e discord.py para realizar a conversão e interagir com o ambiente do Discord.

### Funções 

- **ConvertFastaToGenbank**: Essa classe representa um cog (módulo) do bot do Discord e contém o comando `ConvertFasta_GenBank`. Essa função recebe um arquivo Fasta enviado como anexo no Discord, converte-o para o formato GenBank utilizando a função `SeqIO.convert()` da biblioteca BioPython e envia o arquivo GenBank convertido de volta ao usuário.

- **ConvertFasta_GenBank**: Esse é o comando propriamente dito, decorado com `@commands.command("FastaToGenbank")`. Ele recebe o contexto (`ctx`) e o arquivo Fasta como um objeto `discord.Attachment`. Em seguida, lê o conteúdo do arquivo, salva-o temporariamente, realiza a conversão para GenBank utilizando `SeqIO.convert()`, envia o arquivo GenBank convertido de volta ao usuário e, por fim, exclui os arquivos temporários.

- **setup**: Essa função é responsável por registrar o cog `ConvertFastaToGenbank` no bot do Discord.

### Utilização

Para utilizar o comando, envie um arquivo Fasta como anexo em uma mensagem no Discord com o comando `FastaToGenbank`. O bot realizará a conversão para GenBank e enviará o arquivo convertido de volta ao usuário.

## Comando de Conversão de Arquivos GenBank para Fasta

Este comando permite a conversão de arquivos GenBank enviados ao bot em arquivos Fasta. Ele utiliza as bibliotecas BioPython e discord.py para realizar a conversão e interagir com o ambiente do Discord.

### Funções

- **ConvertGenbankToFasta**: Essa classe representa um cog (módulo) do bot do Discord e contém o comando `ConvertFasta_GenBank`. Essa função recebe um arquivo GenBank enviado como anexo no Discord, converte-o para o formato Fasta utilizando a função `SeqIO.convert()` da biblioteca BioPython e envia o arquivo Fasta convertido de volta ao usuário.

- **ConvertFasta_GenBank**: Esse é o comando propriamente dito, decorado com `@commands.command("GenbankToFasta")`. Ele recebe o contexto (`ctx`) e o arquivo GenBank como um objeto `discord.Attachment`. Em seguida, lê o conteúdo do arquivo, salva-o temporariamente, realiza a conversão para Fasta utilizando `SeqIO.convert()`, envia o arquivo Fasta convertido de volta ao usuário e, por fim, exclui os arquivos temporários.

- **setup**: Essa função é responsável por registrar o cog `ConvertGenbankToFasta` no bot do Discord.

### Utilização

Para utilizar o comando, envie um arquivo GenBank como anexo em uma mensagem no Discord com o comando `GenbankToFasta`. O bot realizará a conversão para Fasta e enviará o arquivo convertido de volta ao usuário.

Lembre-se de ter as bibliotecas BioPython e discord.py instaladas para executar o comando corretamente.
