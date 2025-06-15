from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Awaitable,
    Optional,
    Type,
    TypeVar,
)

from mixer.backend.sqlalchemy import Mixer
from mixer.main import LOGGER
from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from fastapi_toolkit.db import BaseModel


TargetT = TypeVar('TargetT')


class AsyncProxyMixer:
    def __init__(
            self,
            mixer: AsyncMixer,
            count: int = 5,
            guards: Optional[tuple[list, dict]] = None
    ):
        self.count = count
        self.mixer = mixer
        self.guards = guards

    async def blend(
            self,
            scheme: Type[BaseModel],
            **values
    ) -> list[Awaitable]:
        if self.guards:
            return await self.mixer._guard(scheme, self.guards, **values)

        return [
            await self.mixer.blend(scheme, **values) for _ in range(self.count)
        ]


class AsyncMixer(Mixer):
    @property
    def session(self) -> Optional[AsyncSession]:
        return self.params.get('session')

    @property
    def commit(self) -> bool:
        return self.params.get('commit') or False

    async def _postprocess(self, target: TargetT) -> TargetT:
        if self.commit:
            session = self.session
            if not session:
                LOGGER.warning(
                    "'commit' set true but session not initialized."
                )
            else:
                session.add(target)
                await session.commit()

        return target

    def postprocess(self, target: TargetT) -> TargetT:
        return self._postprocess(target)

    def cycle(self, count: int = 5) -> AsyncProxyMixer:
        return AsyncProxyMixer(self, count)
