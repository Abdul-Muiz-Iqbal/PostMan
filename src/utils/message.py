from dataclasses import dataclass
from utils import Member, Status
from typing import Any
import arrow, cryptography.fernet as fernet

@dataclass
class Message:
    """Represents a text message sent by the user."""
    content: str
    author: Member
    time_of_arrival: arrow.Arrow
    status: Status

    def as_dict(self) -> dict[str, str]:
        """Converts self to a dictionary compatible with the middleman."""
        return {
            'content': str(self.content),
            'author': str(self.author),
            'time_of_arrival': str(self.time_of_arrival),
            'status': str(self.status)
        }

    @staticmethod
    def from_dict(d: dict[str, Any]) -> 'Message':
        """Converts dictionary into self for deserialization."""
        return Message(
            content = d['content'],
            author = d['author'],
            time_of_arrival = d['time_of_arrival'],
            status = d['status']
        )

    def encrypted(self, key: bytes) -> 'Message':
        """Encrypts the content field of the message and returns a copy."""
        crypter = fernet.Fernet(key)
        return Message(
            content = crypter.encrypt(self.content.encode()).decode('utf-8'),
            author = self.author,
            time_of_arrival = self.time_of_arrival,
            status = self.status 
        )

    def decrypted(self, key: bytes) -> 'Message':
        """Decrypts the content field of the message and returns a copy."""
        crypter = fernet.Fernet(key)
        return Message(
            content = crypter.decrypt(self.content.encode()).decode('utf-8'),
            author = self.author,
            time_of_arrival = self.time_of_arrival,
            status = self.status
        )