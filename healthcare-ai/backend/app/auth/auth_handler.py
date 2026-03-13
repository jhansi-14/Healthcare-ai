from jose import jwt
SECRET="secret123"
ALGORITHM="HS256"
def create_token(data:dict):
    token=jwt.encode(data,SECRET,algorithm=ALGORITHM)
    return token