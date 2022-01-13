# Design Pattern - Strategy

O Strategy nos oferece uma maneira flexível para escrever diversos algoritmos diferentes, e de passar esses algoritmos para classes clientes que precisam deles. Esses clientes desconhecem qual é o algoritmo "real" que está sendo executado, e apenas manda o algoritmo rodar. Isso faz com que o código da classe cliente fique bastante desacoplado das implementações dos algoritmos, possibilitando assim com que esse cliente consiga trabalhar com N diferentes algoritmos sem precisar alterar o seu código.


### Se eu tenho apenas uma única estratégia, faz sentido implementar o Strategy?

Se é nítido que novas estratégias aparecerão, com certeza um Strategy é mais limpo do que um conjunto de ifs, 