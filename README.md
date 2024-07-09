<p align="center" style="margin: 40px 0">
    <img src="./doc-images/logo.svg" height="100px">
</p>

<div align="center">

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![sqlalchemy](https://img.shields.io/badge/SQLAlchemy-D71F00.svg?style=for-the-badge&logo=SQLAlchemy&logoColor=white)

</div>

# Agriprecision - Serviço de Colheitas em Talhões

Seu plantio sustentável e eficiente.

**Agriprecision** tem como objetivo contribuir para a agricultura de precisão, definindo os requisitos das safras e do solo para se obter uma produtividade eficiente, com a preservação de recursos e assegurar a sustentabilidade ambiental. Assim, contribuindo para [o documento da ONU dos Objetivos de Desenvolvimento Sustentável](https://brasil.un.org/pt-br/sdgs).

Projeto desenvolvido para o MVP na Sprint: **Arquitetura de Software** da Pós Graduação de Engenharia de Software da PUC-Rio.


## Arquitetura de Software Desenvolvida

O projeto foi desenvolvido em uma arquitetura baseada em microsserviços, na qual uma aplicação front-end monolítica gerencia todo o estado e o comportamento, enquanto utiliza microsserviços de apoio para recuperar dados ou executar as operações necessárias. Os microsserviços utilizados são: Serviço de autenticação, Serviço de dados do clima e Serviço de colheitas em talhões, que podem ser observados melhor no diagrama a seguir.

![diagrama da arquitetura](./doc-images/arq-diagram.jpg)


### Acesso aos componentes da Arquitetura

- [Aplicação Front-end](https://github.com/MicaelRiboura/agriprecisionWebApp)
- **Serviço de Colheitas em Talhões (Repositório Atual)**
-  [Serviço de Autenticação de Usuário](https://github.com/MicaelRiboura/agriPrecisionUserService)
-  [Serviço de Clima de Open Weather API](https://github.com/MicaelRiboura/agriprecisionWebApp/blob/develop/weather-api.docs.md)

## Como Executar a Aplicação com Docker

### 1 - Clonando o repositório
Antes de tudo, precisamos clonar o projeto para ser executado em sua máquina. Você pode clonar esse repositório fazendo o download por meio de um arquivo ZIP ou através do seguinte comando:

```
git clone https://github.com/MicaelRiboura/learn-with-me-api.git
```

> ⚠️ Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

### 2 - Criando a imagem Docker
Primeiro, você deve criar uma imagem Docker com o seguinte comando:

```
docker build -t agri-harvest-service .
```

### 3 - Rodando container Docker
Para executar um container Docker com base na imagem criada através do seguinte comando:

```
docker run -p 5001:5000  agri-harvest-service
```

Ao final, cole esse endereço no seu navegador para visualizar a documentação da API e suas rotas:

```
localhost:5001
```

## Como Executar a Aplicação sem Docker

### 1 - Clonando o repositório
Antes de tudo, precisamos clonar o projeto para ser executado em sua máquina. Você pode clonar esse repositório fazendo o download por meio de um arquivo ZIP ou através do seguinte comando:

```
git clone https://github.com/MicaelRiboura/learn-with-me-api.git
```

> ⚠️ Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

#

Para executar a aplicação é necessário ter todas as libs (bibliotecas) python listadas no arquivo `requirements.txt` instaladas. 

#

### 2 - Criando um ambiente virtual (opcional)

Para a instalação das dependências da aplicação, é **fortemente recomendado** a criação de um ambiente virtual python. Esse ambiente tem como objetivo dar mais liberdade de utilizar diferentes bibliotecas e até versões da linguagem Python, sem que haja conflito entre elas.

Você pode criar um  ambiente virtual a partir do seguinte comando:

```
python -m venv env
```

Após criar o ambiente virtual, você pode ativá-lo a partir do seguinte comando:

```
# Windows:
.\env\Scripts\activate.ps1

# Linux ou Mac:
source ./python_env/bin/activate
```

> ⚠️ Esse é um passo opcional, mas fortemente recomendável.

### 3 - Instalando as dependências

Para instalar as libs listadas no arquivo `requirements.txt`, execute o comando abaixo:

```
(env)$ pip install -r requirements.txt
```
### 4 - Executando a API
Finalmente, para executar a API, basta executar o seguinte comando:

```
(env)$ flask run --host 0.0.0.0 --port 5001
```

Em modo de desenvolvimento, é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte, conforme abaixo:

```
(env)$ flask run --host 0.0.0.0 --port 5001 --reload
```

Ao final, cole esse endereço no seu navegador para visualizar a documentação da API e suas rotas:

```
localhost:5001
```

> ⚠️ O símbolo *(env)$* é apenas para ilustrar um terminal com o virtualenv ativado, não pertencendo aos comandos apresentados acima.
