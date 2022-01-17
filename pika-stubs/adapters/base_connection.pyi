import abc
from typing import Callable, Generic, Sequence, TypeVar

from .. import connection
from .utils import connection_workflow, nbio_interface

_OnCloseCallback = Callable[['BaseConnection', Exception], None]
_OnOpenCallback = Callable[['BaseConnection'], None]
_OnOpenErrorCallback = Callable[['BaseConnection', str | Exception], None]

_IOLoop = TypeVar('_IOLoop')


class BaseConnection(Generic[_IOLoop], connection.Connection):

    def __init__(
        self,
        parameters: connection.Parameters | None,
        on_open_callback: _OnOpenCallback | None,
        on_open_error_callback: _OnOpenErrorCallback | None,
        on_close_callback: _OnCloseCallback | None,
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
                connection.Connection |
                connection_workflow.AMQPConnectionWorkflowFailed |
                connection_workflow.AMQPConnectionWorkflowAborted,
            ],
            None
        ],
        custom_ioloop: _IOLoop | None = ...,
        workflow: connection_workflow.AbstractAMQPConnectionWorkflow | None = ...,
    ) -> connection_workflow.AbstractAMQPConnectionWorkflow: ...

    @property
    def ioloop(self) -> _IOLoop: ...
