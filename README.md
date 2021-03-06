# Design Pattern - Alura

Com o lançamento do livro Design Patterns: Elements of Reusable Object-Oriented Software, em 1995, que os Design Pattern realmente ganharam popularidade no mundo do desenvolvimento de software. Neste livro foram catalogados e descritos vinte e três padrões para o desenvolvimento de software orientado a objetos. Seus autores, Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides, ficaram conhecidos como a “Gangue dos Quatro” (Gang of Four) ou simplesmente GoF. Posteriormente, vários outros livros do estilo foram publicados. Tendo, inclusive, a Sun Microsystems, publicado, em 2002, a primeira edição do livro Core J2EE Patterns: Best Practices and Design Strategies, que catalogou vinte e cinco padrões voltados para o J2EE, utilizando e baseando-se nos padrões GoF.

Neste contexto, a principal vantagem do uso de padrões de projeto está no reuso das soluções propostas para determinado problema, o que permite que até mesmo profissionais menos experientes possam atuar como especialistas. Pois os padrões, geralmente, são frutos da experiência de profissionais experientes que tiveram a oportunidade de aplicar e validar tais soluções em projetos reais. Além disso, podemos destacar a facilitação da manutenção, já que um padrão representa uma unidade de conhecimento comum entre os envolvidos.

A utilização de alguns padrões, apesar de ser benéfica na maioria dos casos, torna o código-fonte maior e mais complexo. Isto nos faz refletir sobre a possibilidade de estarmos desnecessariamente aumentando a complexidade do design. Portanto, é necessário não somente conhecer os padrões de projeto, mas sim, realmente entendê-los para identificar quando utilizá-los e usufruir positivamente da experiência herdada.

Existem muitos padrões de projeto espalhados por aí. Padrões que visam ajudar na solução dos mais diversos tipos de problemas. Como sempre, ao ver um padrão, entenda a motivação do padrão; a razão dele existir. Não vá direto para a implementação. Um padrão é mais do que uma implementação, mas sim um conceito, uma ideia de como resolver um problema. Há também a possibilidade de um padrão de projeto não ser necessário quando algum recurso da linguagem resolve elegantemente o problema em questão. Vimos que isso pode ser verdade em linguagens multiparadigmas como Python.

Mas no final, lembre-se: o que importa é código de qualidade. Se você implementou uma solução que faz uso de boa orientação a objetos ou de recursos bem aplicados da programação funcional, não tem problema; o seu código e os outros desenvolvedores agradecem mesmo assim!


## 1 - Strategy

O Strategy nos oferece uma maneira flexível para escrever diversos algoritmos diferentes, e de passar esses algoritmos para classes clientes que precisam deles. Esses clientes desconhecem qual é o algoritmo "real" que está sendo executado, e apenas manda o algoritmo rodar. Isso faz com que o código da classe cliente fique bastante desacoplado das implementações dos algoritmos, possibilitando assim com que esse cliente consiga trabalhar com N diferentes algoritmos sem precisar alterar o seu código.

### Se eu tenho apenas uma única estratégia, faz sentido implementar o Strategy?

Se é nítido que novas estratégias aparecerão, com certeza um Strategy é mais limpo do que um conjunto de ifs,

## 2 - Chain of Responsibility

O padrão Chain of Responsibility cai como uma luva quando temos uma lista de comandos a serem executados de acordo com algum cenário em específico, e sabemos também qual o próximo cenário que deve ser validado, caso o anterior não satisfaça a condição.

A intenção do Chain of Responsabilidade não é dividir a responsabilidade em fatias menores e sim criar uma cadeia de decisão onde cada objeto representa uma responsabilidade.

Nesses casos, o Chain of Responsibility nos possibilita a separação de responsabilidades em classes pequenas e enxutas, e ainda provê uma maneira flexível e desacoplada de juntar esses comportamentos novamente.

Como nesse incremento, em relação a aula 1, os descontos formam como se fosse uma "corrente", ou seja, um ligado ao outro. Daí o nome do padrão de projeto: Chain of Responsibility. A ideia do padrão é resolver problemas como esses: de acordo com o cenário, devemos realizar alguma ação. Ao invés de escrevermos código procedural, e deixarmos um único método descobrir o que deve ser feito, quebramos essas responsabilidades em várias diferentes classes, e as unimos como uma corrente.

### Reflita: qual é a diferença entre uma estratégia e uma cadeia do padrão Chain of Responsibility?

Lembrando, no padrão Strategy cada algoritmo (cada estratégia) é encapsulado em uma classe ou função. No capítulo anterior vimos que cada classe/função implementou um cálculo de imposto (ICMS, ISS etc).

No Chain of Responsibility cada "estratégia" também possui a responsabilidade de descobrir se ela deve ser aplicada e, caso não aplique, delegar para a próxima. Por isso tem nas classes como DescontoPorItens aquele if, e por isso ela deve saber do próximo

## 3 - Template Method

repare que os dois novos impostos adicionados no arquivo `impostos.py`, apesar de diferentes, possuem uma estrutura em comum. Ambos checam o orçamento para ver se devem cobrar a taxação máxima e, a partir daí, cobram a máxima ou a mínima.

Podemos generalizar a estrutura do nosso código e criar um template para esses dois cálculos que utilizaria a mesma base um método calcula, um para validação se deve usar a taxa máxima (retorna um bool) e outros dois para calcular a taxa máxima e outro para a taxa mínima. Logo, podemos tornar esses métodos abstratos!

Veja que ambos as classes de impostos só implementam as partes "que faltam" do algoritmo! A classe Template_de_imposto_condicional possui um método que funciona como um template, ou seja, um molde, para as classes filhas. Daí o nome do padrão de projeto: Template Method.

### Quando usar o Template Method?

Quando temos diferentes algoritmos que possuem estruturas parecidas, o Template Method é uma boa solução. Com ele conseguimos definir em um nível mais macro a estrutura do algoritmo, deixando "buracos" que serão implementados de maneira diferente por cada uma das implementações específicas.

Dessa forma, reutilizamos o nosso código ao invés de repeti-lo, facilitando possíveis evoluções, tanto do algoritmo em sua estrutura macro, quanto dos detalhes do algoritmo, já que cada classe tem sua responsabilidade bem separada.

## 4 - Decoradores

Em muitos projetos, pode ser necessário criar comportamentos que sejam compostos por outros comportamentos. Um exemplo seria calcularmos o ICMS em cima do ISS.

O Decorator é para compor e dividir comportamento em fatias onde cada fatia (objeto) representa uma parte da responsabilidade. Os Decorators modificam/melhoram o comportamento original.

### Quando devemos aplicar o padrão Decorator?

Sempre que percebemos que temos comportamentos que podem ser formados por comportamentos de outras classes envolvidas em uma mesma hierarquia, como foi o caso dos impostos, que podem ser composto por outros impostos. O Decorator introduz a flexibilidade na composição desses comportamentos, bastando escolher no momento da instanciação, quais instancias serão utilizadas para realizar o trabalho.

## 5 - State

Nossos orçamentos podem ter diferentes estados durante o seu ciclo de vida. Um orçamento nasce "Em aprovação" e pode virar "Aprovado" ou "Reprovado". Ao final de todo o processo, deverá ser "Finalizado". Dependendo do estado que o orçamento se encontra, algumas ações podem ser diferentes.
A longo prazo é importante pensar na manutenção do seu código, tendo em vista a certeza de que seu código vai mudar. A solução procedural é fácil de se implementar, mas difícil de manter. Já, a consideração da aplicação de um padrão de projeto pode ser demorada, mas surte efeitos na manutenção e legibilidade do seu código.

### Quando devemos aplicar o padrão State?

A principal situação que faz emergir o Design Pattern State é a necessidade de implementação de uma máquina de estados. Geralmente, o controle das possíveis transições entre estados são várias, também são complexas, fazendo com que a implementação não seja simples. O State auxilia a manter o controle dos estados simples e organizados, através da criação de classes que representem cada estado e sabendo controlar as transições entre eles.

## 6 - Builder

Use o padrão Builder quando você quer que seu código seja capaz de criar diferentes representações do mesmo produto (por exemplo, casas de pedra e madeira). O padrão Builder pode ser aplicado quando a construção de várias representações do produto envolvem etapas similares que diferem apenas nos detalhes.

### Quando devemos aplicar o padrão Builder?

Sempre que tivermos um objeto complexo de ser criado, que possui diversos atributos, ou que possui uma lógica de criação complicada, podemos esconder tudo isso em um Builder.

Porém, na linguagem Python, esse pattern muitas vezes é desnecessário, já que parâmetros nomeados e opcionais do construtor de classes podem muitas vezes lidar com a complexidade de criação do objeto.

## 7 - Observer
O Observer desacopla seu código e possibilita que seu código execute diferentes ações após algum evento. Além disso, como o código demonstrar, criar e executar novas ações é uma tarefa fácil agora.

### Quando devemos aplicar o padrão Observer?
Quando o acoplamento da nossa classe está crescendo, ou quando temos diversas ações diferentes a serem executadas após um determinado processo. Nestes casos, podemos implementar o Observer.

Ele permite que diversas ações sejam executadas de forma transparente à classe principal, reduzindo o acoplamento entre essas ações, facilitando a manutenção e evolução do código.

## Conclusão
Padrões de projeto trazem grande flexibilidade ao seu código, mas isso tem um preço: complexidade. Naturalmente um código que faz uso de padrões de projeto é, do ponto de vista de implementação, mais complexo do que um código que não os utiliza. Afinal, como tudo está desacoplado, o desenvolvedor precisa entender melhor a solução para entender o que o código faz como um todo.

Um bom desenvolvedor sabe fazer essa avaliação e entender quais os ganhos e perdas da utilização de um padrão. Em um problema simples de resolver, talvez o uso de um padrão de projeto não faça sentido; o código vai apenas ficar mais complicado. Agora, em problemas que são por natureza complexos, ou que demandam flexibilidade, pois mudam o tempo todo, talvez a utilização de um padrão de projeto traga benefícios, já que todos os padrões sempre agregam flexibilidade ao código gerado.