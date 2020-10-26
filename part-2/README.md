## The Problem

Recebemos um dump com lista de URLs de imagens de produtos que vamos utilizar para manter nossa base de dados atualizada.
Este dump contém imagens de milhões de produtos e URLs, e é atualizado a cada 10 minutos:

```json
{"productId": "pid2", "image": "http://www.linx.com/6.png"}
{"productId": "pid1", "image": "http://www.linx.com/1.png"}
{"productId": "pid1", "image": "http://www.linx.com/2.png"}
{"productId": "pid1", "image": "http://www.linx.com/7.png"}
{"productId": "pid1", "image": "http://www.linx.com/3.png"}
{"productId": "pid1", "image": "http://www.linx.com/1.png"}
{"productId": "pid2", "image": "http://www.linx.com/5.png"}
{"productId": "pid2", "image": "http://www.linx.com/4.png"}
```

As URLs pertencem a uma empresa terceirizada que hospeda a maioria destas imagens, e ela nos cobra um valor fixo por cada request.
Já sabemos que o dump de origem não tem uma boa confiabilidade, pois encontramos várias imagens repetidas e boa parte delas também retornam status 404.
Como não é interessante atualizar nossa base com dados ruins, precisamos enviar apenas com URLs que retornam status 200.
O processo de atualização ocorre também através de um dump, onde o formato é ligeiramente diferente da entrada:

```json
{"productId": "pid1", "images": ["http://www.linx.com/1.png", "http://www.linx.com/2.png", "http://www.linx.com/7.png"]}
{"productId": "pid2", "images": ["http://www.linx.com/3.png", "http://www.linx.com/5.png", "http://www.linx.com/6.png"]}
```

Para diminuir a quantidade de requests necessárias para validar as URLs, decidimos limitar a quantidade de imagens por produto em até 3.
O seu objetivo é criar um software que gera o dump agregado no menor tempo possível e com o mínimo de requests desnecessárias (já que existe um custo fixo por requisição).

## Dependencies

- Python3
- Redis
- Ruby

## SetUp 

For this project, you'll need to setupt three thigs. First, start redis in your local machine. You can do it following the Quickstart on redis official page [(doc)](https://redis.io/topics/quickstart): 

```bash
$ wget http://download.redis.io/redis-stable.tar.gz
$ tar xvzf redis-stable.tar.gz
$ cd redis-stable
$ make
$ redis-server
```

After this, you will need to run the ruby service provided by the DL team. Making sure you have the sinatra gem installed:

```bash 
$ ruby ruby_service/url-aggregator-api.rb 
```

At last, you'll need to install the python3 requirements file, run:

```bash
pip install -r requirements.txt
```

## Usage

To use this service, make sure that both redis and the ruby services are running, and then run the following command:

```bash 
$ python src/main.py src/dump/input-dump
```

After the service is finished running, an **output.json** file will be createed at the [/src/dump](/src/dump) folder and the runtime of the script will be displayed in the terminal.

Obs¹: I believe that in Ubuntu, python3.XX is called with **python3** 

Obs²: You can chance the argument `src/dump/input-dump` for another json file that have the same structure as the one passed as example.

## Testing

To run the tests, make sure that **Usage** segment is done, and run:

```bash
$ cd test/; python -m unittest; cd .. 
```

## Obstacles

In this section i'll write a bit about the things i notice that are not ideal for a service like this. Basically describing some points I know that i have to improve

--- **Testing** - The second part was a harder for me to structure the project to make it testable. I end up only making tests for some of the functions in the Class file

--- **Performance** - I'm not really happy with the performance of my service. with my tests i get in avarege *80 seconds* to finish the job. Python is known to be slower then some other langagues. But i think there's still room for performance gain. I tried porting the service to use threads, but i could't find a way to do it without having the risk of overrind something in Redis. 