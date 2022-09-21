Dividir Grandes Databases.

Esta é uma simples, porém eficaz solução para dividir uma base de dados grande.
Em um cenário que existe uma base de dados .csv muito grande, é possível dividir essa base
em quantas partes forem necessárias.

Com o pandas, usei a propriedade iloc[], onde você consegue definir o tamanho em linhas, de
cada arquivo.

Neste código, peguei uma tabela com 234 linhas e dividi em duas partes, a primeira com 100 linhas
e a segunda com o restante

<img src='https://github.com/guilhermebrumatti/guilhermebrumatti/blob/main/Screenshot_3.jpg' />


