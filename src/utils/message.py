from dataclasses import dataclass, asdict
from utils import Member, Status
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
        return { field: str(value) for field, value in asdict(self).items() }

    def from_dict(self, d: dict[str, str]) -> 'Message':
        """Converts dictionary into self for deserialization."""
        return Message(
            content = d['content'],
            author = d['author'],
            time_of_arrival = d['time_of_arrival'],
            status = d['status']
        )

    def encrypted(self, key: str) -> 'Message':
        """Encrypts the content field of the message and returns a copy."""
        crypter = fernet.Fernet(key)
        return Message(
            content = crypter.encrypt(self.content),
            author = self.author,
            time_of_arrival = self.time_of_arrival,
            status = self.status 
        )

    def decrypted(self, key: str) -> 'Message':
        """Decrypts the content field of the message and returns a copy."""
        crypter = fernet.Fernet(key)
        return Message(
            content = crypter.decrypt(self.content),
            author = self.author,
            time_of_arrival = self.time_of_arrival,
            status = self.status
        )