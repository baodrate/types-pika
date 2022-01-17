from __future__ import annotations

import ssl
from socket import socket
from typing import Any
from typing import Callable

from . import nbio_interface

def check_callback_arg(callback: Callable[..., Any], name: str) -> None: ...
def check_fd_arg(fd: int) -> None: ...

class SocketConnectionMixin:
    def connect_socket(
        self, sock: socket, resolved_addr: Any, on_done: Callable[[BaseException | None], None]
    ) -> nbio_interface.AbstractIOReference: ...

class StreamingConnectionMixin:
    def create_streaming_connection(
        self,
        protocol_factory: Callable[[], nbio_interface.AbstractStreamProtocol],
        sock: socket,
        on_done: Callable[
            [BaseException | tuple[nbio_interface.AbstractStreamTransport, nbio_interface.AbstractStreamProtocol]], None
        ],
        ssl_context: ssl.SSLContext | None = ...,
        server_hostname: str | None = ...,
    ) -> nbio_interface.AbstractIOReference: ...
