Django Jogo de Cartas
=====================

Um jogo de cartas para praticar testes e patterns em nosso time de desenvolvimento interno Nokia.
A ideia é criar um jogo semelhante o Jogo Magic ou HeartStone da Blizzard

Regras
======
- Maximo: 2 jogadores.
- Cada Jogador tem 20 pontos de vida.
- Cada jogador tem que criar um ou mais decks de cartas.
- Cada carta possui 2 attributos (ataque, vida, elemento)
- O gasto de mana de cada carta é referente ao maior atributo que ele criou.
- O usuário só pode selecionar uma Magia extra para cada carta.
- Cada Deck não pode fechar com mais de 2 cartas com a mesma mágia.
- Cada rodada o jogador ganha 1 ponto de mana totalizando 8 pontos no máximo.
- Criação de carta o usuário pode destruir uma carta que ele ganhou em um jogo para montar outra
com os pontos armazenados das cartas.
- No seu turno, o jogador pode usar ataque as cartas algumas cartas podem ter poderes atingir o personagem.
- Ganha a partida quem acabar com todos os pontos de vida do oponente.
- Além de ataques físicos, podem ser usadas cartas em seus turnos para ataque, defesa ou mudança de status. Categorias de cartas:
    - Elemento  (terra, fogo, água, ar, sagrado, demoniaca)
    - Status Negativo (dormir, veneno, etc…)
    - Status Positivo (cura, recuperação de mana)
