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


router = APIRouter()


@router.post(
    "/pet2",
    responses={
        200: {"model": Pet, "description": "successful operation"},
        405: {"description": "Invalid input"},
    },
    tags=["pet"],
    summary="Add a new pet to the store",
    response_model_by_alias=True,
)
async def add_pet2(
    pet: Pet = Body(None, description="Pet object that needs to be added to the store"),
):
    return {
        "test":"sucess"
    }
    """"""
    ...
