import hashlib

def hash_data(data: str):
    return hashlib.sha256(data.encode()).hexdigest()

def mask_data(data: str):
    return data[:2] + "****" + data[-2:]