from enum import Enum

class Status(Enum):
    """Enumerates against every possible status a message can have:\n
    Deleted -> Message has been deleted\n
    Read    -> Message has been read and is queued for deletion\n
    Unread  -> Message is unread and is cached in the database\n
    Unsent  -> Message not sent due to lack of an internet connection"""
    Deleted = 0
    Read    = 1
    Unread  = 2
    Unsent  = 3

    def __repr__(self) -> str:
        return self.name