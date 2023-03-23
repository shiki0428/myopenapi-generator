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



async def add_pet2(
    pet: Pet = Body(None, description="Pet object that needs to be added to the store"),
    db: Session = Depends(crud.get_db)
):
    """"""
    a = db.query(crud.User).filter(crud.User.email == 'string').first()
    print(a)

    return {}
    ...
