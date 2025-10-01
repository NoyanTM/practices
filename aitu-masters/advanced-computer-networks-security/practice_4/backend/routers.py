from fastapi import APIRouter, Depends

from backend.auth import require_roles, Token, get_current_user

router = APIRouter()

@router.get("/health")
async def health():
    return {"message": "ok"}

@router.get("/me")
def get_current(current_user: Token = Depends(get_current_user)):
    return {"token": current_user}

@router.get("/protected/user", dependencies=[Depends(require_roles("ROLE_USER", "ROLE_ADMIN"))])
def user():
    return {"message": "user"}

@router.get("/protected/admin", dependencies=[Depends(require_roles("ROLE_ADMIN"))])
def admin():
    return {"message": "admin"}
