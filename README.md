Antes de começar verifique os requisitos do projeto:
```
-Python 3.13.3 (ou qualquer versão Python 3.x compatível)

```




-🧪 Pergunta 1
Escreva uma função que determina se uma string termina com ‘A’ e começa com 'B'.<br>

-📐 Pergunta 2
Considere a sequência numérica:
11, 18, 25, 32, 39...
Crie uma função que recebe como entrada uma posição e devolve o valor correspondente naquela posição da sequência, considerando que a sequência começa na posição 1.

🔍 Exemplos:
print_valor(x=1) retornará 11

print_valor(x=2) retornará 18

print_valor(x=200) retornará 1404

print_valor(x=254) retornará 1782

print_valor(x=3542158) retornará 24.795.110
<br>


🧠 Lógica da Solução
Para encontrar qualquer número da sequência em uma determinada posição, usamos a lógica da progressão aritmética, que consiste em somar a razão (7) repetidamente a partir do valor inicial (11).
No entanto, como o primeiro número da sequência já é o valor da posição 1, a lógica aplicada é:
A cada nova posição, somamos 7 ao número anterior.
Ou seja, o valor da posição n é igual a 11 + (n - 1) × 7.




-🎲 Pergunta 3
Simulação de um jogo com tabuleiro unidirecional para dois jogadores.

Regras:
Vence quem alcançar a última casa com o menor número de turnos.

A movimentação é feita por uma roleta que sorteia os valores 1, 2 ou 3 casas.

Se o jogador tirar um número maior que as casas restantes, ele:

Caminha até a última casa,

Volta ao início,

E anda o restante das casas, iniciando novamente o percurso (looping).

Requisitos da função:
Receber o número de casas do tabuleiro (mínimo: 3) e retornar:

* Quantidade mínima de turnos para vencer (caminho ótimo)

* Probabilidade de executar o caminho ótimo

* Número total de caminhos possíveis sem looping

🧠 Lógica da Solução
Neste jogo, o jogador sorteia em cada turno um número entre 1 e 3 casas para avançar. O objetivo é alcançar a última casa do tabuleiro com o menor número de turnos possíveis (caminho ótimo).
Porém, se o jogador tirar um valor maior que as casas restantes, ele é obrigado a voltar ao início (looping), o que torna o caminho inválido.
A solução envolve três partes:
Quantidade mínima de turnos:
Calculada considerando que o jogador tira 3 em todos os turnos, que é o valor máximo possível.
Fórmula: ceil(número_de_casas / 3)
Probabilidade de seguir o caminho ótimo:
Calculamos todas as formas possíveis de chegar exatamente à última casa com o mínimo de turnos, e comparamos com o total de combinações possíveis para esse número de turnos.
Total de caminhos sem looping:
Contamos quantas sequências de jogadas existem que levam à última casa sem ultrapassá-la em nenhum momento.



-💼 Pergunta 4
Escreva uma função que calcula o valor a receber ao pedir demissão, considerando:

Férias proporcionais:
Zeram a cada aniversário de contratação (o funcionário sempre tirou as férias corretamente).

Décimo Terceiro proporcional:
Zerado a cada virada de ano (1º de janeiro), ou seja, não acumula de um ano para o outro.

A função deve considerar:
Salário mensal

Data de admissão

Data de demissão

E retornar:

Valor proporcional de férias

Valor proporcional do 13º salário

Total a receber no momento da rescisão



🧠 Lógica da Solução
As férias são calculadas com base no número de meses trabalhados desde o último aniversário de contratação.
A cada 12 meses trabalhados, o funcionário tem direito a 1 salário de férias.
Ao ser demitido, ele recebe o valor proporcional aos meses incompletos do novo ciclo.

* Exemplo:
Se a admissão foi em março e a demissão em agosto do ano seguinte, ele trabalhou 5 meses após o último aniversário de empresa → recebe 5/12 do salário como férias proporcionais.


O 13º salário é baseado nos meses trabalhados no ano da demissão, contando a partir de janeiro até o mês da demissão.
A cada mês trabalhado no ano, o funcionário tem direito a 1/12 do salário.
Ao ser demitido em agosto, por exemplo, recebe 8/12 do salário como 13º proporcional.
