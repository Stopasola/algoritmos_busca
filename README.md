Para executar o código, basta executar a função main, ela irá carregar as informações correspondente aos dados do
grafo (graph_list.csv) e as coordenadas de cada nó (coordinatres.csv).
Será retornado o custo total para as bsucas A* e busca em profundidade.

Obs: para a leitura correta dos arquivos csv, é necessário adicionar duas linahs em branco após o grafo inserido.
Obs2: É possivel que seja necessário instalar o package csv para executar o programa em algumas máquinas, para tal
é necessário executar os seguintes comando.

>> pip install pip
>> pip install csv


grap_structure  {'Frankfurt': {'Wurzburg': 111, 'Mannheim': 85}, 'Wurzburg': {'Nurnberg': 104, 'Stuttgart': 140, 'Ulm': 183}, 'Mannheim': {'Nurnberg': 230, 'Karlsruhe': 67}, 'Karlsruhe': {'Basel': 191, 'Stuttgart': 64}, 'Nurnberg': {'Ulm': 171, 'Munchen': 170, 'Passau': 220}, 'Stuttgart': {'Ulm': 107}, 'Basel': {'Bern': 91, 'Zurich': 85}, 'Bern': {'Zurich': 120}, 'Zurich': {'Memmingen': 184}, 'Memmingen': {'Ulm': 55, 'Munchen': 115}, 'Munchen': {'Ulm': 123, 'Passau': 189, 'Rosenheim': 59}, 'Rosenheim': {'Salzburg': 81}, 'Passau': {'Linz': 102}, 'Salzburg': {'Linz': 126}}

{'Frankfurt': {'Wurzburg': 111, 'Mannheim': 85}, 'Wurzburg': {'Nurnberg': 104, 'Stuttgart': 140, 'Ulm': 183}, 'Mannheim': {'Nurnberg': 230, 'Karlsruhe': 67}, 'Karlsruhe': {'Basel': 191, 'Stuttgart': 64}, 'Nurnberg': {'Ulm': 171, 'Munchen': 170, 'Passau': 220}, 'Stuttgart': {'Ulm': 107}, 'Basel': {'Bern': 91, 'Zurich': 85}, 'Bern': {'Zurich': 120}, 'Zurich': {'Memmingen': 184}, 'Memmingen': {'Ulm': 55, 'Munchen': 115}, 'Munchen': {'Ulm': 123, 'Passau': 189, 'Rosenheim': 59}, 'Rosenheim': {'Salzburg': 81}, 'Passau': {'Linz': 102}, 'Salzburg': {'Linz': 126}}


![image](https://user-images.githubusercontent.com/17886190/160051673-bff395e7-4997-40e7-8bfa-afcd1c98e867.png)


altamira,cascavel,20
altamira,brusque,10
brusque,diadema,50
brusque,esmeralda,10
cascavel,diadema,20
cascavel,esmeralda,33
diadema,esmeralda,5
diadema,florianopolis,12
esmeralda,florianopolis,1
esmeralda,altamira,12
florianopolis,cascavel,22


altamira,24,52
brusque,27,49
cascavel,25,53
diadema,23,46
esmeralda,28,51
florianopolis,27,48
