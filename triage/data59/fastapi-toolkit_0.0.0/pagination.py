from typing import (
    List,
    Union,
)

from pydantic import (
    BaseModel,
    Field,
    create_model,
)


class BaseMeta(BaseModel):
    count: int


class PageNumberPagination(BaseMeta):
    page: int = Field(None, gt=0)
    page_size: int = Field(None, gt=0)


class LimitOffsetPagination(BaseMeta):
    limit: int = Field(None, gt=0)
    offset: int = Field(None, ge=0)


class Meta(BaseModel):
    __root__: Union[LimitOffsetPagination, PageNumberPagination]


def pagination_model(model, prefix=''):
    return create_model(
        f'{prefix}Pagination{model.__name__}',
        meta=(Meta, ...),
        result=(List[model], ...)
    )
