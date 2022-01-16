# Design Pattern - Alura

## Strategy - Aula 1

O Strategy nos oferece uma maneira flexível para escrever diversos algoritmos diferentes, e de passar esses algoritmos para classes clientes que precisam deles. Esses clientes desconhecem qual é o algoritmo "real" que está sendo executado, e apenas manda o algoritmo rodar. Isso faz com que o código da classe cliente fique bastante desacoplado das implementações dos algoritmos, possibilitando assim com que esse cliente consiga trabalhar com N diferentes algoritmos sem precisar alterar o seu código.


### Se eu tenho apenas uma única estratégia, faz sentido implementar o Strategy?

Se é nítido que novas estratégias aparecerão, com certeza um Strategy é mais limpo do que um conjunto de ifs, 

## Chain of Responsability - aula 2


O padrão Chain of Responsibility cai como uma luva quando temos uma lista de comandos a serem executados de acordo com algum cenário em específico, e sabemos também qual o próximo cenário que deve ser validado, caso o anterior não satisfaça a condição.

Nesses casos, o Chain of Responsibility nos possibilita a separação de responsabilidades em classes pequenas e enxutas, e ainda provê uma maneira flexível e desacoplada de juntar esses comportamentos novamente.

Como nesse incremento, em relação a aula 1, os descontos formam como se fosse uma "corrente", ou seja, um ligado ao outro. Daí o nome do padrão de projeto: Chain of Responsibility. A ideia do padrão é resolver problemas como esses: de acordo com o cenário, devemos realizar alguma ação. Ao invés de escrevermos código procedural, e deixarmos um único método descobrir o que deve ser feito, quebramos essas responsabilidades em várias diferentes classes, e as unimos como uma corrente.


### Reflita: qual é a diferença entre uma estratégia e uma cadeia do padrão Chain of Responsibility?

Lembrando, no padrão Strategy cada algoritmo (cada estratégia) é encapsulado em uma classe ou função. No capítulo anterior vimos que cada classe/função implementou um cálculo de imposto (ICMS, ISS etc).

No Chain of Responsibility cada "estratégia" também possui a responsabilidade de descobrir se ela deve ser aplicada e, caso não aplique, delegar para a próxima. Por isso tem nas classes como DescontoPorItens aquele if, e por isso ela deve saber do próximo