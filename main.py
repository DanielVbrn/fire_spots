import pandas as pd
from redis_connection import connect_to_redis
from redis_service import RedisService

# Conectar ao Redis
redis_client = connect_to_redis()

# Criar uma instância do RedisService
redis_service = RedisService(redis_client)

# Consultas usando os métodos do serviço
focos_por_estado = redis_service.get_focos_por_estado()
print("\nFocos de incêndio por estado:")
print(focos_por_estado)

focos_por_municipio = redis_service.get_focos_por_municipio()
print("\nFocos de incêndio por município:")
print(focos_por_municipio)

risco_fogo_medio = redis_service.get_risco_fogo_medio_por_estado()
print("\nMédia de risco de fogo por estado:")
print(risco_fogo_medio)

precipitacao_media_bioma = redis_service.get_precipitacao_media_por_bioma()
print("\nMédia de precipitação por bioma:")
print(precipitacao_media_bioma)

focos_por_mes = redis_service.get_focos_por_mes()
print("\nFocos de incêndio por mês:")
print(focos_por_mes)

# Exportar para Excel
with pd.ExcelWriter('relatorio_focos_incendio.xlsx') as writer:
    focos_por_estado.to_frame(name='Focos por Estado').to_excel(writer, sheet_name='Estado')
    focos_por_municipio.to_frame(name='Focos por Município').to_excel(writer, sheet_name='Município')
    risco_fogo_medio.to_frame(name='Risco Médio de Fogo').to_excel(writer, sheet_name='Risco de Fogo')
    precipitacao_media_bioma.to_frame(name='Precipitação Média por Bioma').to_excel(writer, sheet_name='Precipitação Bioma')
    focos_por_mes.to_frame(name='Focos por Mês').to_excel(writer, sheet_name='Focos por Mês')

print("Relatório gerado e exportado para 'relatorio_focos_incendio.xlsx'")
