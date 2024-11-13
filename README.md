# Sistema de Monitoramento de Focos de Incêndio
## [Base de dados do INPE](https://terrabrasilis.dpi.inpe.br/queimadas/bdqueimadas/)

Este projeto é um sistema de monitoramento de focos de incêndio que utiliza dados de incêndios em tempo real, armazenados no Redis, e exibe um dashboard interativo para visualização e análise dos dados. O sistema processa informações sobre focos de incêndio, como data, localização, risco de fogo, precipitação, e outros dados geográficos.

O objetivo é fornecer uma interface visual que permita acompanhar de forma clara e interativa as informações dos focos de incêndio, incluindo métricas como:
- Contagem de focos de incêndio por estado e município.
- Média de risco de fogo por estado.
- Média de precipitação por bioma.
- Distribuição dos focos de incêndio ao longo dos meses.

## Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas:

- `Flask`: Servidor web para fornecer uma API e hospedar o dashboard.
- `Dash`: Framework de visualização interativa para criar o dashboard.
- `Redis`: Banco de dados em memória para armazenamento rápido e acesso dos dados.
- `Pandas`: Biblioteca para manipulação e análise de dados.
- `Plotly`: Biblioteca para geração de gráficos e visualizações interativas no dashboard.

## Estrutura do Projeto

O projeto está dividido nos seguintes arquivos:

- `main.py`: Ponto de entrada do sistema. Configura o servidor Flask e o dashboard Dash.
- `redis_connection.py`: Contém funções para conectar ao Redis e manipular os dados.
- `redis_service.py`: Define consultas específicas para os dados armazenados no Redis.
- `focos_incendio.csv`: Arquivo de dados dos focos de incêndio (necessário para carregar dados no Redis). 


## Instalação

Para configurar o ambiente, siga estas etapas:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
