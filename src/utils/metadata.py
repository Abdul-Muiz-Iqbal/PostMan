from dataclasses import dataclass, asdict
from utils import Member

@dataclass
class MetaData:
    members: list[Member]
    server_name: str

    @staticmethod
    def from_dict(d: dict[str, str]) -> 'MetaData':
        return MetaData(
            members = d['members'],
            server_name = d['server_name']
        )

    def as_dict(self) -> dict[str, str]:
        return { field: str(value) for field, value in asdict(self).items() }