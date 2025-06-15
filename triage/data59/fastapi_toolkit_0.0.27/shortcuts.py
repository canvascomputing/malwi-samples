from typing import (
    Type,
    Union,
)

from fastapi import (
    HTTPException,
    status as statuses,
)

from fastapi_toolkit.crud.base import (
    CRUDBase,
    ModelType,
)
from fastapi_toolkit.db.base_class import BaseModel

__all__ = (
    'get_object_or_404',
)


def _get_model_name(model_class: Union[CRUDBase, Type[BaseModel]]) -> str:
    if hasattr(model_class, 'model'):
        model_class = model_class.model
    return model_class.__table__.name


async def get_object_or_404(
        crud: CRUDBase,
        condition=None,
        session=None
) -> ModelType:
    obj = await crud.get(condition, session=session)
    if not obj:
        raise HTTPException(
            statuses.HTTP_404_NOT_FOUND,
            detail=f'Object does not exist in '
                   f'table {_get_model_name(crud.model)}'
        )
    return obj
