from dataclasses import dataclass

@dataclass
class Member:
    """The anonymous user who has written a specific message.
    Also represents a user who is online."""
    username: str
    is_admin: bool = False

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Member):
            return NotImplemented
        return self.username == o.username

    def __str__(self) -> str:
        return f'{self.username}'