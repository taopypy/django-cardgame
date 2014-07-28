django-cardgame
================

Um jogo de cartas para praticar testes e patterns em nosso time de desenvolvimento interno Nokia.

Regras
======
- Maximo: 2 jogadores.
- Cada jogador começa com 20 pontos para distribuir entre 4 habilidades: ataque, mana, defesa e vida.
- No seu turno, o jogador pode usar ataque físico contra o outro ou uma carta. - Um ataque físico tira pontos de vida. O dano sofrido pelo jogador será o status de ataque do oponente versus o seu status de defesa. A cada 3 ataques o atacante sobe 1 nível, e ganha 4 pontos para distribuir entre suas habilidades. Ganha a partida quem acabar com todos os pontos de vida do oponente.
- Além de ataques físicos, podem ser usadas cartas em seus turnos para ataque, defesa ou mudança de status. Categorias de cartas: Magia (terra, fogo, água, ar), Status Negativo (sleep, poison, etc…), Status Positivo (cura, recuperação de mana).
