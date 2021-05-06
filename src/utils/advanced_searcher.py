from dataclasses import dataclass
from typing import Optional
from utils import MessageId, Status, Member
import arrow

@dataclass
class AdvancedSearcher:
    """Builder class for a Message allowing for advanced search capabilities."""
    name: Optional[Member]
    content: Optional[str]
    id: Optional[MessageId]
    time_of_arrival: Optional[arrow.Arrow]
    status: Optional[Status]

    def as_dict(self) -> dict[str, str]:
        d = {}
        if self.name: d['author'] = str(self.name)
        if self.content: d['content'] = self.content
        if self.id: d['_id'] = str(self.id)
        if self.time_of_arrival: d['time_of_arrival'] = str(self.time_of_arrival)
        if self.status: d['status'] = str(self.status)

        return d