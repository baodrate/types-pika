from __future__ import annotations

import asyncio
from collections.abc import Sequence
from typing import Callable

from .. import connection
from . import base_connection
from .utils import connection_workflow

_OnCloseCallback = Callable[[AsyncioConnection, Exception], None]
_OnOpenCallback = Callable[[AsyncioConnection], None]
_OnOpenErrorCallback = Callable[[AsyncioConnection, str | Exception], None]

class AsyncioConnection(base_connection.BaseConnection[asyncio.AbstractEventLoop]):
    def __init__(
        self,
        parameters: connection.Parameters | None = ...,
        on_open_callback: _OnOpenCallback | None = ...,
        on_open_error_callback: _OnOpenErrorCallback | None = ...,
        on_close_callback: _OnCloseCallback | None = ...,
        custom_ioloop: asyncio.AbstractEventLoop | None = ...,
        internal_connection_workflow: bool = ...,
    ) -> None: ...
    @classmethod
    def create_connection(
        cls,
        connection_configs: Sequence[connection.Parameters],
        on_done: Callable[
            [
                connection.Connection
                | connection_workflow.AMQPConnectionWorkflowFailed
                | connection_workflow.AMQPConnectionWorkflowAborted
            ],
            None,
        ],
        custom_ioloop: asyncio.AbstractEventLoop | None = ...,
        workflow: connection_workflow.AbstractAMQPConnectionWorkflow | None = ...,
    ) -> connection_workflow.AbstractAMQPConnectionWorkflow: ...
