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
from models.item import Item


from common.router.custom_api_router import CustomAPIRouter
router = CustomAPIRouter()

async def add_item(
) -> List[Item]:
    """"""
    ...
