from abc import ABC, abstractmethod
from typing import Iterable
from utils import Message, MessageId, AdvancedSearcher, MetaData

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