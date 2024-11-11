import redis
import json
import pandas as pd
from redis_connection import connect_to_redis

# Conectar ao Redis
redis_client = connect_to_redis()

class RedisService:
    
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def get_all_focos(self):
        """Retorna todos os focos de incêndio armazenados no Redis como DataFrame."""
        retrieved_records = []
        for key in self.redis_client.scan_iter("foco_incendio:*"):
            retrieved_records.append(json.loads(self.redis_client.get(key)))
        
        # Garantir que a coluna 'DataHora' seja convertida para datetime
        df = pd.DataFrame(retrieved_records)
        df['DataHora'] = pd.to_datetime(df['DataHora'], format='%Y/%m/%d %H:%M:%S')
        return df

    def get_focos_por_estado(self):
        """Retorna a contagem de focos por estado."""
        df = self.get_all_focos()
        return df['Estado'].value_counts()

    def get_focos_por_municipio(self):
        """Retorna a contagem de focos por município."""
        df = self.get_all_focos()
        return df['Municipio'].value_counts()

    def get_risco_fogo_medio_por_estado(self):
        """Retorna a média de risco de fogo por estado."""
        df = self.get_all_focos()
        return df.groupby('Estado')['RiscoFogo'].mean()

    def get_precipitacao_media_por_bioma(self):
        """Retorna a média de precipitação por bioma."""
        df = self.get_all_focos()
        return df.groupby('Bioma')['Precipitacao'].mean()

    def get_focos_por_mes(self):
        """Retorna a contagem de focos por mês."""
        df = self.get_all_focos()
        
        # Garantir que a coluna 'DataHora' esteja no formato datetime
        df['DataHora'] = pd.to_datetime(df['DataHora'], errors='coerce')  # Converte novamente se necessário
        return df.groupby(df['DataHora'].dt.to_period('M')).size()

    # Outros métodos específicos de consulta podem ser adicionados aqui
