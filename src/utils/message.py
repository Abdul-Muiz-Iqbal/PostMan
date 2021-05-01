from dataclasses import dataclass
from utils import Author, Status
import arrow

@dataclass
class Message:
    """Represents a text message sent by the user."""
    content: str
    author: Author
    time_of_arrival: arrow.Arrow
    status: Status

    def as_dict(self) -> dict[str, str]:
        """Converts self to a dictionary compatible with the middleman."""
        return {
            'content': self.content,
            'author': str(self.author),
            'time_of_arrival': str(self.time_of_arrival),
            'status': str(self.status)
        }

    def from_dict(self, d: dict[str, str]) -> 'Message':
        """Converts dictionary into self for deserialization."""
        return Message(
            content = d['content'],
            author = d['author'],
            time_of_arrival = d['time_of_arrival'],
            status = d['status']
        )