## Simulador PokePython
Um simulador de batalhas Pokémon em Python

- Link para testar o jogo (Notebook no Google Colab): http://tiny.cc/TestePokePython
- Para a utilização do programa, execute o arquivo pokepython.py com o Python3.
- A escolha dos Pokémon é de acordo com o nome do Pokémon em inglês e com as iniciais em maiúsculo (Bulbasaur, Ho-Oh, etc.).

Notas sobre a atual versão:
- Após a escolha dos Pokémon, surgirá uma mensagem de erro, pois a última implementação mudou a apresentação de alguns dados, o que tá dando algum trabalho para fazer as novas associações.

Este é um projeto de um iniciante em programação, feito com o intúito de aprender as diversas possibilidades na programação. :)

A motivação veio com o início do aprendizado sobre a programação orientada a objetos, então surgiu a ideia de simular uma batalha Pokémon semelhante à que ocorre nos jogos da primeira geração quando se escolhe o Pokémon inicial. Está disponível o arquivo do protótipo com esta versão inconcluída.

Com o decorrer do projeto, surgiram ideias que levaram o conceito do jogo a outro nível.
A nova ideia foi utilizar um dataset disponibilizado na internet (https://www.kaggle.com/mylesoneill/pokemon-sun-and-moon-gen-7-stats/) como base para alimentar o programa. Neste dataset estão os dados dos Pokémon até a sétima geração (Pokémon Sun e Pokémon Moon). Todos os arquivos .csv vieram desta fonte, apesar de alguns arquivos terem sido modificados com ajustes para se adequar à programação utilizada.

As demandas do projeto são:
1. ~Registrar os Pokémons no programa.~ (ok)
2. ~Registrar os golpes no programa.~ (ok)
3. Fazer os ajustes nos Pokémons escolhidos pelo usuário. (Ex.: Level, golpes, natureza, atributos...) (Em progresso)
- OBS: já concluído: level, atributos base, MoveSet.
- Escolher 4 golpes entre os possíveis para o Pokémon (de forma aleatória? escolhendo um por um? escolhendo os últimos que o Pokémon aprendeu naquele level?)
- Importar a natureza dos pokémons.
- Nova demanda: Aplicar um algorítimo que faça os atributos do pokémon crescerem de acordo com o level escolhido.
4. Criar um algorítimo para o funcionamento da batalha com uma mecânica semelhante à mecânica de batalha dos jogos clássicos. (Basear no protótipo.)
5. Importar a tabela de multiplicador de dano entre tipos. 
6. Criar um algorítimo que escolha o Pokémon que irá agir primeiro.
7. Criar um algorítimo que cause o dano no Pokémon adversário.
8. Criar um algorítimo que cause buffs/debuffs/efeitos negativos(dormir/envenenamento/congelamento...).
9. Qualquer demanda que surgir durante o desenvolvimento.

A utilização de qualquer coisa protegida por direitos autorais neste projeto não possui intenção comercial. A decisão de utilização dos Pokémons para este programa veio pela minha paixão pela franquia, por conhecimento de boa parte das mecânicas do jogo e com intúito de aprender novas coisas sobre programação seguindo as demandas do programa. :)
