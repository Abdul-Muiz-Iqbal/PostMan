from dataclasses import dataclass, asdict
from typing import Any
from utils import Member

@dataclass
class MetaData:
    members: list[Member]
    server_name: str

    @staticmethod
    def from_dict(d: dict[str, Any]) -> 'MetaData':
        return MetaData(
            members = d['members'],
            server_name = d['server_name']
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            'members': list(map(str, self.members)),
            'server_name': self.server_name
        }