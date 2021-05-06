from typing import Iterable, Optional
from utils import Message, MessageId, AdvancedSearcher, MetaData
from abcs import MiddleMan
import pymongo

class MongoServer(MiddleMan):
    """The MiddleMan which uses MongoDb as its server."""

    def __init__(self, uri: str, database: str, collection: str) -> None:
        """Initializes the MongoClient and creates references to a db and collection."""
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[database]
        self.msgs = self.db[collection]
        self.__metadata = None

    def add(self, document: Message) -> MessageId:
        """Add a message into the database and return a unique id for it."""
        return MessageId(self.msgs.insert_one(document.as_dict()).inserted_id)

    def remove(self, id: MessageId) -> bool:
        """Remove a message from the database using a unique id and return success or failure."""
        return self.msgs.delete_one({'_id': id._id}).deleted_count > 0

    def find(self, search_criteria: AdvancedSearcher) -> Iterable:
        """Find a specific message or list of messages using a search criteria."""
        return self.msgs.find(search_criteria.as_dict())

    @property
    def metadata(self) -> Optional[MetaData]:
        """Get the metadata from the database.
        The MetaData collection will always have only one document."""
        if self.__metadata is not None:
            m = self.db['MetaData'].find({ 'id': self.__metadata })[0]
            return MetaData.from_dict(m)
        return None

    @metadata.setter
    def metadata(self, m: MetaData):
        """Sets/edits the metadata in the db.
        Since this collection always has only one document, it first clears out the previous one."""
        if self.__metadata is not None:
            self.metadata.drop()
        self.__metadata = self.db['MetaData'].insert_one(m.as_dict()).inserted_id