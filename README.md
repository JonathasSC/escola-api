<div align='center'>

# Escola API REST

#### API usando Django Rest Framework

</div>

<hr>

### :computer:Tecnologias Utilizadas:

![django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=Django&logoColor=white) ![sqlite](https://img.shields.io/badge/SQLite-003B57.svg?style=for-the-badge&logo=SQLite&logoColor=white) ![git](https://img.shields.io/badge/Git-F05032.svg?style=for-the-badge&logo=Git&logoColor=white)

### :hammer_and_wrench:Ferramentas Utilizadas:

![Visual studio code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white) ![postman](https://img.shields.io/badge/Postman-FF6C37.svg?style=for-the-badge&logo=Postman&logoColor=white)

<hr>

## :arrow_down:Instalação

:warning: Essa instalação é feita baseada no sistema operacional windows.

#### Requisitos:

<li>Git
<li>API Client
<li>Python v3.6X
<li>IDE de sua preferência

#### :eyes:Visualizando API

##### 1. Abra um terminal

Clique com botão direito na sua área de trabalho e clique em "Abrir no terminal".

##### 2. Copie, cole e execute os comandos na sequência:

1. `git clone https://github.com/JonathasSC/escola_api_drf`

2. `cd .\escola_api_drf\`

3. `python -m venv venv`

4. `.\venv\Scripts\activate`

5. `pip install -r requirements.txt`

6. `python .\manage.py runserver`

##### 3. Copie a URL da API.

Após executar os comandos mencionados, verifique se o servidor foi criado e está sendo executado com sucesso. Você encontrará a confirmação indicada pela seguinte mensagem:

`Starting development server at http://127.0.0.1:8000/`

Copie essa parte **http://127.0.0.1:8000/** , ou uma semelhante que lhe seja apresentada, para acessar o servidor localmente.

##### 4. Veja detalhes e endpoints

Cole o URL previamente copiado em seu navegador de preferência e adicione **swagger/** ao final da URL.

##### 5. Mais detalhes e responses

Substitua o'**swagger/** por **redoc/** ao final da URL.

#### :arrow_up_small: Executando requisições para API

Para fazer requisições na API, será necessário o servidor sendo executado enquanto utiliza um API Client.

Para obter acesso completo à API, é necessário incluir no cabeçalho (header) da solicitação o Token de exemplo fornecido, seguindo a seguinte estrutura: " **Token 9d59f3dcbbc79932f87838728953494530f41667** ".

Este token de autorização é essencial para autenticar e autorizar o acesso aos recursos da API.

Caso houver dificuldades de utilizar a API Client, recomendamos essas duas aplicações e seus tutoriais:

**Postman**:
https://learning.postman.com/docs/introduction/overview/

**Insomnia.**:
https://docs.insomnia.rest/insomnia/install
