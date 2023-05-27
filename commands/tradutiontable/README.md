## Comando de Tradução de DNA

Esse comando recebe o ID da tabela de tradução e um arquivo FASTA contendo as sequências a serem traduzidas. A função `traduzir` utiliza a biblioteca BioPython para realizar a tradução das sequências. 

### Tabelas de Tradução Disponíveis

A função de tradução suporta as seguintes tabelas de tradução:
Os seguintes códigos genéticos são descritos aqui:

1. Código Padrão
2. Código Mitocondrial Vertebrado
3. Código Mitocondrial da Levedura
4. Código Mitocondrial de Mofo, Protozoário e Celenterado e o Código Micoplasma/Espiroplasma
5. código mitocondrial de invertebrados
6. Código Nuclear Ciliado, Dasicladáceo e Hexamita
##

9. Código Mitocondrial do Equinodermo e da Planície
10. Código Nuclear Euplóide
11. Código Bacteriano, Archaeal e Plant Plastid
12. Código Nuclear de Levedura Alternativo
13. Código Mitocondrial Ascídico
14. Código Mitocondrial Alternativo de Platelmintos
16. Código mitocondrial clorofíceo
##
21. Código mitocondrial de trematódeos
22. Código Mitocondrial Scenedesmus obliquus
23. Código Mitocondrial Thraustochytrium
24. Código Mitocondrial Rhabdopleuridae
25. Divisão Candidata SR1 e Código Gracilibacteria
26. Código Nuclear de Pachysolen tannophilus
27. Código Nuclear Cariorrelicto
28. Código Nuclear do Condilostoma
29. Código Nuclear do Mesodínio
30. Código Nuclear Peritrich
31. Código Nuclear dos Blastocritídeos
##
33. Cephalodiscidae Mitochondrial UAA-Tyr Code

Elas podem ser encontradas em detalhes aqui: [The Genetic Codes](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)

### Funções Utilizadas

- **traduzir**: Essa função é decorada com `@commands.command("Traduzir")` e representa o comando propriamente dito. Ela recebe o contexto (`ctx`), o ID da tabela de tradução e o arquivo FASTA contendo as sequências. A função lê as sequências do arquivo FASTA e realiza a tradução usando a tabela de tradução selecionada. As sequências traduzidas são armazenadas em uma lista e, em seguida, são salvas em um arquivo de saída. O arquivo de saída é enviado de volta ao usuário no chat.

### Utilização

Para utilizar o comando, digite o comando seguido do ID da tabela de tradução desejada e anexe o arquivo FASTA contendo as sequências a serem traduzidas. Por exemplo: `!Traduzir 1 arquivo.fasta`. O bot realizará a tradução das sequências usando a tabela de tradução selecionada e enviará o arquivo de saída com as traduções de volta ao usuário no chat.
