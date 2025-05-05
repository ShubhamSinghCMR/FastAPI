from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, schemas
from app.core.security import create_access_token, hash_password, verify_password
from app.core.token_blacklist import add_token_to_blacklist
from app.database import get_db
from app.dependencies.auth import oauth2_scheme

router = APIRouter(

    tags=["Auth"],
    responses={401: {"description": "Unauthorized"}, 400: {"description": "Bad Request"}},
)


@router.post(
    "/register",
    response_model=schemas.UserOut,
    summary="Register a new user",
    response_description="User created successfully",
)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user with a **unique email and username**.

    - **username**: Required, unique
    - **email**: Required, must not already be registered
    - **password**: Required, plain text (will be hashed)
    """
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = hash_password(user.password)
    new_user = models.User(
        username=user.username, email=user.email, hashed_password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post(
    "/login",
    response_model=schemas.Token,
    summary="Authenticate a user",
    response_description="JWT token returned on success",
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    Authenticate user and return a **JWT token** if credentials are valid.

    - **username**: Entered as form field (not JSON)
    - **password**: Plain text password
    """
    user = (
        db.query(models.User).filter(models.User.username == form_data.username).first()
    )
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.post(
    "/logout",
    summary="Log out user",
    response_description="Blacklists the current token",
)
def logout(request: Request, token: str = Depends(oauth2_scheme)):
    """
    Invalidate the current access token by adding it to the **blacklist**.

    - Requires Authorization header with Bearer token.
    """
    add_token_to_blacklist(token)
    return {"message": "Successfully logged out"}
