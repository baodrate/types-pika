from __future__ import annotations

from collections.abc import Sequence
from typing import Callable

import tornado.ioloop

from .. import connection
from . import base_connection
from .utils import connection_workflow
from .utils import nbio_interface

_OnCloseCallback = Callable[[TornadoConnection, Exception], None]
_OnOpenCallback = Callable[[TornadoConnection], None]
_OnOpenErrorCallback = Callable[[TornadoConnection, str | Exception], None]

class TornadoConnection(base_connection.BaseConnection[tornado.ioloop.IOLoop]):
    def __init__(
        self,
        parameters: connection.Parameters | None = ...,
        on_open_callback: _OnOpenCallback | None = ...,
        on_open_error_callback: _OnOpenErrorCallback | None = ...,
        on_close_callback: _OnCloseCallback | None = ...,
        custom_ioloop: tornado.ioloop.IOLoop | nbio_interface.AbstractIOServices | None = ...,
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
        custom_ioloop: tornado.ioloop.IOLoop | None = ...,
        workflow: connection_workflow.AbstractAMQPConnectionWorkflow | None = ...,
    ) -> connection_workflow.AbstractAMQPConnectionWorkflow: ...
