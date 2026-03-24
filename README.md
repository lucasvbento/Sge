# SGE - Sistema de Gestão Empresarial

## Descrição
O SGE é uma aplicação desenvolvida para a gestão eficiente de processos empresariais. O projeto utiliza o framework Django e foi estruturado para oferecer tanto uma interface administrativa quanto uma API escalável para integrações externas.

## Tecnologias Utilizadas

### Backend
* Python: Linguagem base do projeto.
* Django: Framework web de alto nível.
* Django Rest Framework (DRF): Toolkit para construção de APIs Web.
* Simple JWT (rest_framework_simplejwt): Implementação de autenticação baseada em tokens JSON Web Token para garantir a segurança dos endpoints da API.

### Frontend
* Bootstrap: Framework CSS utilizado para garantir uma interface responsiva e organizada.

### Infraestrutura
* Docker: Utilizado para a conteinerização da aplicação, garantindo que o ambiente de desenvolvimento seja idêntico ao de produção.
* Docker Compose: Orquestração de serviços necessários para o funcionamento do sistema.

## Funcionalidades Principais
* Gestão de fornecedores (Suppliers) e produtos (Products).
* Autenticação segura via JWT.
* Interface responsiva para dispositivos móveis e desktop.
* Endpoints de API documentados para consumo por outras aplicações.

## Como Executar o Projeto com Docker

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

1. Clone o repositório:
   git clone https://github.com/lucasvbento/Sge.git
   cd Sge

2. Construa e inicie os containers:
   docker-compose up --build

3. Execute as migrações do banco de dados:
   docker-compose exec web python manage.py migrate

4. Acesse a aplicação em seu navegador:
   http://localhost:8000

## Configuração de Ambiente
O projeto utiliza variáveis de ambiente para chaves de segurança e configurações de banco de dados. Um exemplo de configuração pode ser encontrado no arquivo .env.example.