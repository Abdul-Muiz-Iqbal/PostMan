class Member:
    """The anonymous user who has written a specific message.
    Also represents a user who is online."""
    username: str
    is_admin: bool = False

    def __eq__(self, o: 'Member') -> bool:
        return self.username == o.username

    def __repr__(self) -> str:
        return f'{self.username}'