# learnops-jokepo
A simple jokepo game in python

Apredendo a codar: Um pequeno jogo de jokepo

Leia, pode te ajudar: https://python.org.br/introducao/

## Requisitos básicos
- Um sistema para jogar jokepo contra a CPU: https://pt.wikipedia.org/wiki/Pedra,_papel_e_tesoura#:~:text=Pedra%2C%20papel%20e%20tesoura%2C%20tamb%C3%A9m,n%C3%A3o%20requer%20equipamentos%20nem%20habilidade.
- Uma API para jogar e
- Uma API para ver as estatisticas que a CPU está usando para jogar
- Uma API para ver o Score
- Uma interface web para jogar e ver essas informações
## Dicas

### Onde começar a procurar?
https://www.w3schools.com/python/default.asp é uma ótima opção, tem muito conteúdo e de uma forma bem didática

### Configurando o ambiente
- use python 3 (https://www.python.org/downloads/)
  - Linux: https://python.org.br/instalacao-linux/
  - Windows: https://python.org.br/instalacao-windows/
- instale o pip como sudo/administrador (https://pip.pypa.io/en/stable/installing/)
- usar virtualenv para criar o ambiente de desenvolvimento (https://virtualenv.pypa.io/en/latest/installation.html)
- user o fastAPI para fazer as APIs (https://fastapi.tiangolo.com/deployment/)
  
### Vai te evitar dor de cabeça no futuro
- crie classes para os dados que vai guardar em memória e para as respostas
- user o modulo de json do próptio python para fazer as respostas

### Como chamar uma API no python

```python
import requests
import json

req = requests.get("example_url")
response = req.json()

print(response)
```

### Como ativar o virtualenv

```shell
source bin/activate
```

### Como executar a aplicação em modo de web server

```shell
./run.sh
```

Não entendeu qualquer coisa q está escrito aqui? pesquise, leia, anote as dúvidas (qualquer uma) e me pergunte.