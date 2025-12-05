import jwt

def createToken(data):
    token : str = jwt.encode(payload=data, key='secret_key', algorithm='HS256')
    return token

def validateToken(token: str) -> dict:
    data: dict = jwt.decode(token, key='secret_key', algorithms=['HS256'])
    return data