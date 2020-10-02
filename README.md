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
Este bot começou simplesmente comigo a querer fazer algo engraçado com a API do twitter. Do momento em que ficou online, tornou-se óbvio que era um sucesso entre os utilizadores do twitter. No começo era utilizado quando alguém encontrava um tweet que discordava profundamente, mas ao longo do tempo e com o crescimento da sua fanbase, o bot era utilizado mesmo quando não fazia sentido nenhum. Por alguma razão, bots deste género no twitter são escassos *(apesar do quoão fácil são de fazer)*, e isso faz com que toda a gente queira experimentá-lo e eventualmente abusá-lo ao aperceber-se que o bot funcionava 24/7.
A partir do momento em que em apenas um dia tinha centenas de chamadas, foi sempre uma pressão constante: estar atento ao funcionamento do servidor, ver se os limites da API não estavam a ser ultrapassados ,lançar mais updates ao bot, etc... Isto também contribuiu em parte para o término do _badtweet.
Se há algo a retirar aqui, é que se há uma atividade preferida na internet, é tirar o sério às pessoas.
