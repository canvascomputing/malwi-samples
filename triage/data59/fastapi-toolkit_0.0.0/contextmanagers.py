from fastapi import (
    HTTPException,
    status,
)
from sqlalchemy.exc import IntegrityError as DBIntegrityError


class IntegrityError:
    def __init__(self, raise_exc: bool = True):
        self._raise = raise_exc

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._raise and exc_val and isinstance(exc_val, DBIntegrityError):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='\n'.join(exc_val.orig.args)
            )
        return not self._raise
