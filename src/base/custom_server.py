from typing import Iterable
from abcs import MiddleMan
from utils import Message, MessageId, AdvancedSearcher
import requests as rq

class CustomServer(MiddleMan):
    """The CustomServer that acts as a middleman for PostMan."""

    def __init__(self, url: str) -> None:
        self.url = url

    def add(self, document: Message) -> MessageId:
        """Send a request to the server to add a message and receive its unique id."""
        return rq.post(self.url + '/add', data= document.as_dict()).json()._id

    def remove(self, id: MessageId) -> bool:
        """Send a request to the server to remove a message using its unique id."""
        return rq.post(self.url + '/remove', data= { '_id': id._id }).ok

    def find(self, search_criteria: AdvancedSearcher) -> Iterable:
        """Send a request to the server to find a message or list of messages according to
        a search criteria."""
        return rq.post(self.url + '/find', data= search_criteria.as_dict()).json()