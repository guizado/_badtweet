# _badtweet
é um bot para o twitter escrito em python e recorrendo à API do twitter, usado para automatizar o processo de irritar pessoas na rede social.


## Para que serve este bot?

![Exemplo1](https://github.com/guizado/_badtweet/blob/master/exemplos/exemplo1.png?raw=true)   Nesta imagem à direita, podemos observar pessoas a discutir sobre algo desimportante. Até uma delas responder a um tweet com "_badtweet". Com isto, o bot entra em ação, e responde com uma montagem a ridicularizar o que a pessoa que recebeu "_badtweet" disse. 
###### Qual é o uso disto?
Nenhum, apenas uma ferramenta para satirizar tweets, terminar discussões, e incitar galhofa e caos.

###### Mais exemplos:
[1](https://github.com/guizado/_badtweet/blob/master/exemplos/image.png?raw=true) [2](https://github.com/guizado/_badtweet/blob/master/exemplos/exemplo2.png?raw=true) [3](https://github.com/guizado/_badtweet/blob/master/exemplos/exemplo23.png?raw=true)
Os *memes* usados quando o bot recebe uma chamada são escolhidos aleatoriamente de um saco de 60 imagens.

## Mas alguém usa isto?
![proof](https://github.com/guizado/_badtweet/blob/master/exemplos/proof.png?raw=true)

_badtweet esteve operacional entre abril e setembro de 2020. Nesse tempo angariou cerca de 7000 seguidores e foi utilizado aproximadamente 20900 vezes.
## Porque é que parou?
A API do twitter limita o número de calls por aplicação. O _badtweet frequentemente excedia estes limites e por isso ficava horas sem funcionar, culminando no início de setembro quando em apenas 1 hora o bot já excedia os limites, fazendo com que maior parte das pessoas nem conseguisse usá-lo, por esta razão, o bot foi desligado de vez.

## Como funciona?
A biblioteca tweepy é utilizada para aceder à API do twitter, com a ajuda desta biblioteca é feita uma conexão a um endpoint de streaming que detecta um tweet nas seguintes condições: __1__ No tweet encontra-se escrito "_badtweet"; __2__ Este tweet está a responder a um outro tweet, que obrigatoriamente tem de ter texto. Guardamos o texto do tweet cujo o tweet escrito "_badtweet" está a responder, de seguida limpamos este texto para não ter links nem caracteres não ascii.

Prosseguimos escolhendo um *meme* aleatório da nossa diretoria. Em cada imagem encontra-se um [espaço em branco](https://github.com/guizado/_badtweet/blob/master/badtweet/templates/20t.jpg?raw=true) que será preenchido com o texto. Um ficheiro json guarda a informação do espaço a preencher de cada imagem: a sua altura, largura e inclinação. Com estes dados utilizo um algoritmo simples para encontrar o tamanho de letra ideal e dividir o texto em linhas de modo a caber dentro do espaço a preencher. Utilizando a biblioteca pillow, uma imagem com o texto é criada e é depois colada no *meme* finalizando o processo de montagem.

Tendo a nossa imagem pronta, utilizo novamente o tweepy para responder a quem disse "_badtweet" com a montagem.

## Uma "expriência social"
####### De onde surgiu a ideia?
Este bot começou simplesmente comigo a querer fazer algo engraçado com a API do twitter, originalmente não havia o objetivo de "gozar" com as outras pessoas, mas quando estava a pesquisar *memes*, reparei que todos apontavam para essa direção, aí a lâmpada acendeu. 
####### De onde veio o sucesso?
Do momento em que ficou online, tornou-se óbvio que era um sucesso entre os utilizadores do twitter. No começo era utilizado quando alguém encontrava um tweet que discordava profundamente, mas ao longo do tempo e com o crescimento da sua fanbase, o bot era utilizado mesmo quando não fazia sentido nenhum. 
Por alguma razão, bots deste género no twitter são escassos *(apesar do quoão fácil são de programar)*, e isso faz com que toda a gente queira experimentá-lo e eventualmente abusá-lo ao aperceber-se que o bot funcionava 24/7.
####### O que há a aprender aqui?
Ideias complexas fáceis de perceber. Em papel é dificil mas na prática? Quem é que não gosta de ser irritante na internet com o mínimo do esforço? A aleatoriedade dos *memes* incentivava a descoberta, e o próprio uso do bot fazia com que quem fosse a vítima, sentia-se compelido a usar contra alguém.
Acho que houve um culminar de pequenas estratégias acidentais que alguém que procure presença online para a sua aplicação possa anotar.
