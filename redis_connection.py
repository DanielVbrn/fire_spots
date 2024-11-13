import redis
import json
import pandas as pd

def connect_to_redis():
    """Conecta ao Redis e retorna o cliente."""
    return redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def store_data_in_redis(df, redis_client):
    """Armazena os dados do DataFrame no Redis."""
    records = df.to_dict(orient='records')
    
    for i, record in enumerate(records):
        redis_client.set(f'foco_incendio:{i}', json.dumps(record))

def load_csv_to_redis(file_path, redis_client):
    """Carrega dados de um arquivo CSV para o Redis."""
    df = pd.read_csv(file_path)
    store_data_in_redis(df, redis_client)
