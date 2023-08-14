import time
import jwt
from decouple import config
SECRET_KEY = config("secret_key")
ALGORITHM = config("algorithm")
def get_access_token(user_name):
    expire_date_time = time.time() + 600
    print(expire_date_time)
    payload = {
        "expiry": expire_date_time,
        "user_name": user_name
    }
    return jwt.encode(payload,SECRET_KEY, algorithm=ALGORITHM)

def decodeJWT(token) -> dict:
    decode_token = jwt.decode(token,  SECRET_KEY, algorithms=[ALGORITHM])
    if(decode_token['expiry'] >= time.time()):
        print(decode_token)
        return decode_token
    return {}