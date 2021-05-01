class Author:
    """The anonymous user who has written a specific message.
    Also represents a user who is online."""
    username: str

    def __eq__(self, o: 'Author') -> bool:
        return self.username == o.username

    def __repr__(self) -> str:
        return f'{self.username}'