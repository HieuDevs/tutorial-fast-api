from exceptiongroup import catch
import fastapi
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
import config


oauth2_schema = OAuth2PasswordBearer("token")


def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(
        minutes=config.setting.access_token_expire_minutes
    )
    token = jwt.encode(
        {**data, **{"exp": expire}},
        config.setting.secret_key,
        algorithm=config.setting.algorithm,
    )
    return token


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(
            token=token,
            algorithm=[config.setting.algorithm],
            key=config.setting.secret_key,
        )
        id: int = payload["user_id"]
        if not id:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return id


def get_current_user(token: str = fastapi.Depends(oauth2_schema)):
    credentials_exception = fastapi.HTTPException(
        status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_access_token(
        token=token,
        credentials_exception=credentials_exception,
    )
