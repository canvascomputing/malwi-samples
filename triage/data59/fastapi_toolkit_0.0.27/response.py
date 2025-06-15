from fastapi_toolkit.dependencies import BasePagination

__all__ = (
    'api_response',
)


def api_response(data, count=None, pagination: BasePagination = None) -> dict:
    if isinstance(data, (list, tuple)):
        return dict(
            meta=pagination.schema(count=count, **pagination.params),
            result=data
        )
    return data
