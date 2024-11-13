import json
import pandas as pd
from redis_connection import connect_to_redis

class RedisService:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def get_all_focos(self):
        """Recupera todos os dados armazenados no Redis e retorna como um DataFrame."""
        retrieved_records = [
            json.loads(self.redis_client.get(key)) 
            for key in self.redis_client.scan_iter("foco_incendio:*")
        ]
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
        df['Mes'] = df['DataHora'].dt.to_period('M')
        return df.groupby('Mes').size()
