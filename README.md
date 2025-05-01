# Processo seletivo para desenvolvedores da EJ Turing Tecnologia 2025
Bem vindos ao processo seletivo para desenvolvedores da Turing Tecnologia, primeira empresa Jr de T.I da UFERSA, gostamos de desafios e acreditamos que o melhor currículo para um programador é os seus projetos realizados, pensando dessa forma, a inscrição do nosso processo seletivo se dará aqui neste repositório.

## Para se tornar candidato a vaga de Desenvolvedor, siga com atenção os passos abaixo:.

- Faça um Fork neste repositório
- Adicione uma pasta com seu nome
- Crie o projeto dentro desta pasta e no Readme deverá ter as seguintes informações:
- Indique para qual time(backend e frontend) deseja entrar
- Se apresente falando um pouco sobre você
- Comente de forma breve sobre o que realizou no projeto
- Adicione Instruções de como rodar o seu projeto em localhost
- Faça um Pull Request para o mesmo repositório.
- Finalize o projeto até dia 11/05
## Sobre o projeto para o teste :
TESTE BACKEND
--------------------
Desenvolver uma API de um sistema simples de compras com carrinho. O sistema deve possuir/permitir:
- Entidade Produto: Nome, Marca, Preço, Descrição.
- CRUD da entidade Produto
- Entidade Carrinho: Preço Total, Lista de Itens(Produtos)
- Adicionar e remover itens no carrinho
- Mostrar os itens atuais do carrinho
- Especificar quantas unidades de X item o Usuario quer no carrinho
- Ao mostrar os itens, deve ser possível verificar quanto cada pacote de itens está custando.
- Exemplo de resultado final(ignorem o atributo imagens):

![image](https://github.com/user-attachments/assets/d3266951-820e-4792-b094-ce847aed9a87)

## Stack (Preferencial)
- Java 8 ou superior
- PostgreSQL
- Springboot
- JPA

## Testes dos Endpoints
Aqui estão os endpoints recomendadas para o teste, e mesmo que siga elas, ainda é necessário documentar seu código. Caso queira fazer seus próprios, não tem problema, basta documenta-las para realizar-mos o teste.
- POST /produto/save (criar produto)
- PUT /produto/{id}/update (atualizar produto)
- GET /produto/{id} (busca um produto)
- GET /produto/all (busca todos os produto)
- DELETE /produto/{id}/delete (deletar produto)
- POST /carrinho/addProduto/{id}?quantidade={quantidade} (adicionar produto no carrinho)
- DELETE /carrinho/removerProduto/1?quantidade={quantidade} (remover produto do carrinho)
- DELETE /carrinho/limpar (remover todos os produtos do carrinho)
- GET /carrinho/mostrar (busca o carrinho)

TESTE FRONTEND
---------------
Desenvolver a sua própria Landing Page ou Portifólio falando sobre você, conquistas, cursos, experiências... utilizando preferencialmente as seguintes tecnologias:

- HTML
- CSS
- Javascript(Desejável)
- React, Vue, Bootstrap, Materialize ou qualquer outro framework Front-End (É um diferencial)

# Observações
Se ainda não souber utilizar o Git e o Github, aproveite a oportunidade para aprender. São ferramentas essenciais para o mercado de trabalho e você terá que utiliza-las de um jeito ou de outro no futuro.

Grupo no Whatsapp para duvidas
https://chat.whatsapp.com/F5v29wmEyyIDAeQhkaD6eM

Vamo Codar! <3
