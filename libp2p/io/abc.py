from abc import (
    ABC,
    abstractmethod,
)
from typing import Any, Optional


class Closer(ABC):
    @abstractmethod
    async def close(self) -> None: ...


class Reader(ABC):
    @abstractmethod
    async def read(self, n: Optional[int] = None) -> bytes: ...


class Writer(ABC):
    @abstractmethod
    async def write(self, data: bytes) -> None: ...


class WriteCloser(Writer, Closer):
    pass


class ReadCloser(Reader, Closer):
    pass


class ReadWriter(Reader, Writer):
    pass


class ReadWriteCloser(Reader, Writer, Closer):
    @abstractmethod
    def get_remote_address(self) -> Optional[tuple[str, int]]:
        """
        Return the remote address of the connected peer.

        :return: A tuple of (host, port) or None if not available
        """
        ...


class MsgReader(ABC):
    @abstractmethod
    async def read_msg(self) -> bytes: ...


class MsgWriter(ABC):
    @abstractmethod
    async def write_msg(self, msg: bytes) -> None: ...


class MsgReadWriteCloser(MsgReader, MsgWriter, Closer):
    pass


class Encrypter(ABC):
    @abstractmethod
    def encrypt(self, data: bytes) -> bytes: ...

    @abstractmethod
    def decrypt(self, data: bytes) -> bytes: ...


class EncryptedMsgReadWriter(MsgReadWriteCloser, Encrypter):
    """Read/write message with encryption/decryption."""

    conn: Optional[Any]

    def __init__(self, conn: Optional[Any] = None):
        self.conn = conn

    def get_remote_address(self) -> Optional[tuple[str, int]]:
        """Get remote address if supported by the underlying connection."""
        if (
            self.conn is not None
            and hasattr(self, "conn")
            and hasattr(self.conn, "get_remote_address")
        ):
            return self.conn.get_remote_address()
        return None
