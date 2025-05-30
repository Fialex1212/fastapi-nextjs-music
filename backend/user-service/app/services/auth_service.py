from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.deps import get_db
from app.utils.redis import r
from app.utils.security import (
    ALGORITHM,
    OAUTH2_SCHEME,
    SECRET_KEY,
    create_access_token,
    verify_password,
)
from db.crud import get_user_by_email
from models.models import User
from models.schemas import UserLogin, UserWithToken

TOKEN_EXPIRE_TIME = 60 * 30  # IN SEDONCS 1800s, IN MINUTES 30m


def login(data: UserLogin, db: Session) -> UserWithToken:
    user = get_user_by_email(data.email, db)
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})

    r.set(token, user.email, ex=TOKEN_EXPIRE_TIME)

    return UserWithToken(id=user.id, email=user.email, username=user.username, access_token=token)

def logout(token: str = Depends(OAUTH2_SCHEME)):
    r.delete(token)
    return {"detail": "Logged out"}

def get_current_user(
    token: str = Depends(OAUTH2_SCHEME), db: Session = Depends(get_db)
):
    if not r.get(token):
        raise HTTPException(status_code=401, detail="Token expired or invalid")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
