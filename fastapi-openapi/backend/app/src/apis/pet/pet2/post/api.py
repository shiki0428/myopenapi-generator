# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from models.extra_models import TokenModel  # noqa: F401
from models.pet import Pet


from common.router.custom_api_router import CustomAPIRouter
router = CustomAPIRouter()

from . import crud
from sqlalchemy.orm import Session

from common.database.database import get_db

async def add_pet2(
    pet: Pet = Body(None, description="Pet object that needs to be added to the store"),
    db: Session = Depends(get_db)
):
    """"""
    a = db.query(crud.User).filter(crud.User.email == 'dd').first()
    print(a)

    return {"id":a.id}
    ...
