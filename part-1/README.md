# The Problem:

Precisamos de uma API para receber a atualização de dados cadastrais de produtos. Ela deve receber um corpo no formato JSON, onde o tamanho varia desde alguns poucos Kb até alguns Gb. Experiências anteriores mostram que alguns clientes costumam enviar o mesmo corpo repetidas vezes ao longo de um curto espaço de tempo.
Isso nos causou alguns problemas, como o fato de ter que escalar nossos bancos de dados muito além do necessário afim de aguentar a carga extra desnecessária.
Para evitar que isto ocorra, precisamos que esta API negue requisições que tem o mesmo corpo num intervalo de 10 minutos.

Aqui está um exemplo do comportamento esperado:
```bash
# 2018-03-01T13:00:00 - primeira requisição, durante 10 minutos requests com o mesmo corpo serão negadas
curl -XPOST http://your-api.chaordic.com.br/v1/products -d '[{"id": "123", "name": "mesa"}]' #=> 200 OK

# 2018-03-01T13:09:59 - mesmo corpo que a request anterior.
curl -XPOST http://your-api.chaordic.com.br/v1/products -d '[{"id": "123", "name": "mesa"}]' #=> 403 Forbidden

# 2018-03-01T13:10:00 - agora a API deve voltar a aceitar o corpo
curl -XPOST http://your-api.chaordic.com.br/v1/products -d '[{"id": "123", "name": "mesa"}]' #=> 200 OK
```
Como esta API atenderá milhares de requisições simultâneas, ela precisa funcionar em um cluster.
É esperado que o comportamento descrito acima se mantenha, independente do nó que receber a requisição.

## Dependencies

- Docker
- Docker-compose

There're some technologies used in this solution that are only needed and provided inside the docker contaier, like: [FastAPI](https://fastapi.tiangolo.com/), [Redis](https://redis.io/) and [Uvicorn](https://www.uvicorn.org/).

## Usage

To run this solution you just need to call:
```bash
$ docker-compose up
```
This will spin up the service at `0.0.0.0:80/v1/products` that you can make POST requests. 

## Testing

To run the tests, after the step above, run:

```bash
$ docker run part-1_web bash -c 'cd test/; python -m unittest'
```
## Obstacles 

In this section i'll write a bit about the things i notice that are not ideal for a service like this. Basically describing some points I know that i have to improve

--- **Imports in python** - There're two instances in the project that is needed to `cd` inside the specific folder to run it properly. I don't believe this is ideal, and probably a better knowledge about imports would remedy that

-- **Tests in general** - Only my second time coding tests for a project. I still can't adapt my project to be fully tested. And some tests are a bit weird (like the POST request test, there're test code inside the prod code).