

Todo mundo já jogou ou conhece o jogo da velha, certo!
Pegando essa base, o projeto desenvolve o jogo com uma base de inteligência, para que o 
player jogue diretamente com a máquina. Mas a máquina não podia perder.

Tendo um exemplo mais claro da estrutura do projeto.
Abra o google e digite na barra de busca “jogo da velha”, o jogo será 
carregado na página de resultado.
Você pode jogar com “X” ou “O”. Por padrão você inicia sendo o “X”. 
A representação do jogo no google tem 3 níveis, fácil, médio e impossível.

Na opção “impossible” se torna impossível ganhar da máquina. Isso acontece 
porque o jogo da velha é formado por uma matriz 3x3, assim gerando nove 
campos ou espaços para serem jogados. Quando a primeira posição é preenchida, 
restam oito, na segunda restam sete, na terceira, seis e assim por diante. 
Tendo assim um  total de 9 preenchimentos, com elementos da primeira  à  
nona posição, gerando um fatorial de nove.

Entretanto no jogo da velha os elementos se repetem, sendo eles “X” e “O”. 
Ficando 5 elementos iguais contra 4. Mas como os símbolos são iguais, quaisquer 
alterações entre um ou outro em um tabuleiro completo não ira alterar sua configuração.

Pois bem, levando em conta os dois símbolos distintos, teremos 5 fatoriais para ‘X’ 
e 4 fatorial para o círculo. Assim, para cada configuração estabelecida, existem 5!x4! 
possibilidades de combinações iguais, levando em conta que são apenas dois símbolos.

Então, para chegar ao número exato de possibilidades jogáveis, devemos pegar 9!/5!x4!
Tendo assim 126 maneiras diferentes de resultados no jogo da velha. Desta forma fica 
fácil para a máquina encontrar a maneira de vencer ou de empatar.

O código é estruturado no conceito do algoritmo de [Minimax](https://en.wikipedia.org/wiki/Minimax), 
não foi construído na fórmula do Minimax, mas o conceito é o mesmo. O código é separado 
em dois arquivos, jogoVelha.py que é onde ocorre o jogo e o IA.py que gera a resposta 
da máquina depois de analisar o mapa do tabuleiro.

Obs. Este projeto é de quando estava na faculdade. Por tanto sua estrutura e conceitos 
podem ser rústicos. Mas decidi não alterar, pois me traz nostalgia.
