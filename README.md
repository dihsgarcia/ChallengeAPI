# Challenge API

Api para gerenciar equipamentos e  estoques.

Com autenticação via token JWT, e controle de acessos com base nas regra de usuario. 

-------------------------------------

## Dependências

- É necessário possuir uma instância do banco de dados PostgreSQL para criação e manipulação dos dados. Um script de criação (CREATE) e carga inicial das tabelas encontra-se na raiz do projeto, dentro da pasta **scriptsDB.**
<br/>

- Também é necessário configurar a variável DATABASE_URL no arquivo de configurações **settings.json**, com a connection string da instância do banco de dados PostgreSQL. 
<br/>

- Dentro do projeto, encontram-se dois arquivos para o **Postman**, um de collection e outro de environments, já com todos os endpoints mapeados e pré-configurados para facilitar os testes.
    - **Exemplo:** o endpoint de login já está configurado para capturar o token gerado e utilizá-lo automaticamente na autenticação dos demais endpoints.

-----------------------------------

## Explicação das decisões técnicas

Essa foi a primeira API que desenvolvi com Python, utilizando o framework FastAPI. Encarei o projeto como um desafio pessoal, já que todas as tecnologias envolvidas eram novas para mim. Mesmo assim, busquei aplicar conceitos que já tenho experiência, como a Clean Architecture, organizando o projeto em camadas bem definidas e separando as responsabilidades em pastas que representam as abstrações de dados e regras de negócio. Meu objetivo foi manter o código modular, de fácil manutenção e escalável, mesmo sendo em um  contexto de aprendizado.