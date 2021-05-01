from bson.objectid import ObjectId
from dataclasses import dataclass

@dataclass
class MessageId:
    """Id of a Message. Is always unique and created automatically by MongoDb, or a Server"""
    _id: ObjectId