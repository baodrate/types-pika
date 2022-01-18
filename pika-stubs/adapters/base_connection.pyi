from __future__ import annotations

import abc
from collections.abc import Sequence
from typing import Callable
from typing import Generic
from typing import TypeVar

from .. import connection
from .utils import connection_workflow
from .utils import nbio_interface

_IOLoop = TypeVar("_IOLoop")

class BaseConnection(Generic[_IOLoop], connection.Connection):
    def __init__(
        self,
        parameters: connection.Parameters | None,
        on_open_callback: Callable[[BaseConnection[_IOLoop]], None] | None,
        on_open_error_callback: Callable[[BaseConnection[_IOLoop], str | Exception], None] | None,
        on_close_callback: Callable[[BaseConnection[_IOLoop], Exception], None] | None,
        nbio: nbio_interface.AbstractIOServices,
        internal_connection_workflow: bool,
    ) -> None: ...
    @classmethod
    @abc.abstractmethod
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
        custom_ioloop: _IOLoop | None = ...,
        workflow: connection_workflow.AbstractAMQPConnectionWorkflow | None = ...,
    ) -> connection_workflow.AbstractAMQPConnectionWorkflow: ...
    @property
    def ioloop(self) -> _IOLoop: ...
