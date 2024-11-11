import redis
import json
import pandas as pd  # Importando pandas aqui

def connect_to_redis():
    """Conecta ao Redis e retorna o cliente."""
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    return redis_client

def store_data_in_redis(df, redis_client):
    """Armazena os dados do DataFrame no Redis."""
    records = df.to_dict(orient='records')
    
    for i, record in enumerate(records):
        redis_client.set(f'foco_incendio:{i}', json.dumps(record))

def retrieve_data_from_redis(redis_client):
    """Recupera os dados armazenados no Redis e retorna como um DataFrame."""
    retrieved_records = []
    
    for key in redis_client.scan_iter("foco_incendio:*"):
        retrieved_records.append(json.loads(redis_client.get(key)))
    
    return pd.DataFrame(retrieved_records)  # Agora pandas (pd) está importado corretamente
