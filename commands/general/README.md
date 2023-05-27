
## Comando de Tamanho de Sequência

Esse comando recebe uma sequência como argumento e retorna o tamanho dessa sequência em bases. A função `length` utiliza a biblioteca BioPython para criar um objeto `Seq` a partir da sequência informada. Em seguida, o tamanho da sequência é obtido usando a função `len` e enviado de volta ao usuário no chat.

### Funções Utilizadas

- **length**: Essa função é decorada com `@commands.command("Tamanho")` e representa o comando propriamente dito. Ela recebe o contexto (`ctx`) e a sequência como argumentos. Em seguida, cria um objeto `Seq` a partir da sequência informada e obtém o tamanho da sequência usando a função `len`. Por fim, envia a mensagem com o tamanho da sequência de volta ao usuário no chat.

### Utilização

Para utilizar o comando, digite o comando seguido da sequência desejada. Por exemplo: `!Tamanho ATCGGTAT`. O bot retornará a mensagem no chat informando o tamanho da sequência.


## Comando de Reverse Complement

Esse comando recebe uma sequência como argumento e retorna o seu reverse complement. A função `ReverseComplement` utiliza a biblioteca BioPython para criar um objeto `Seq` a partir da sequência informada. Em seguida, é aplicada a função `reverse_complement` para obter o reverse complement da sequência. O resultado é enviado de volta ao usuário no chat.

### Funções Utilizadas

- **ReverseComplement**: Essa função é decorada com `@commands.command("RVC")` e representa o comando propriamente dito. Ela recebe o contexto (`ctx`) e a sequência como argumentos. Em seguida, cria um objeto `Seq` a partir da sequência informada e aplica a função `reverse_complement` para obter o reverse complement da sequência. Por fim, envia a mensagem com o reverse complement da sequência de volta ao usuário no chat.

### Utilização

Para utilizar o comando, digite o comando seguido da sequência desejada. Por exemplo: `!RVC ATCGGTATTCA`. O bot retornará a mensagem no chat com o reverse complement da sequência.
