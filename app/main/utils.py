import hashlib

def get_hash_name(name:str, salt:str) -> str:
    return str(hashlib.sha256((salt + name).encode()).hexdigest())