from abc import ABC, abstractmethod
from typing import Iterable
from utils import Message, MessageId, AdvancedSearcher, MetaData, Member

class MiddleMan(ABC):
    """Details the inteface a server should have for communication between users in PostMan."""

    @abstractmethod
    def add(self, document: Message) -> MessageId:
        pass

    @abstractmethod
    def remove(self, id: MessageId) -> bool:
        pass

    @abstractmethod
    def find(self, search_criteria: AdvancedSearcher) -> Iterable:
        pass

    @property
    @abstractmethod
    def metadata(self) -> MetaData:
        pass

    @metadata.setter
    @abstractmethod
    def metadata(self, m: MetaData):
        pass

    @property
    def members(self) -> list[Member]:
        return self.metadata.members

    @members.setter
    def members(self, members: list[Member]):
        self.metadata = MetaData(
            members = members,
            server_name = self.server_name
        )

    @property
    def server_name(self) -> str:
        return self.metadata.server_name

    @server_name.setter
    def server_name(self, server_name: str):
        self.metadata = MetaData(
            members = self.members,
            server_name = server_name
        )