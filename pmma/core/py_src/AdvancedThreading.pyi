import threading
from typing import Any, Callable

class AdvancedThread(threading.Thread):
    def __init__(
        self,
        group: None = ...,
        target: Callable[..., Any] | None = ...,
        name: str | None = ...,
        args: tuple[Any, ...] = ...,
        kwargs: dict[str, Any] | None = ...,
        *,
        daemon: bool | None = ...,
    ) -> None: ...

    def kill(self) -> None: ...