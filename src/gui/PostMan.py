from base import MongoServer
from utils import Message, Status, MetaData
import arrow, threading
import webview, arrow

class PrimitiveApi():

    def __init__(self):
        self.server = None
        self.username = None

    def getMetadata(self) -> dict[str, str]:
        if self.server is None:
            self.initializeServer()

        m = self.server.metadata
        return {
            'members': list(map(str, m.members)),
            'server_name': m.server_name
        }

    def setMetadata(self, m: dict[str, str]):
        if self.server is None:
            self.initializeServer()
        self.server.metadata = MetaData(
            members = m['members'],
            server_name = m['server_name']
        )

    def isValidUri(uri: str):
        try:
            self.server = MongoServer(uri = uri, database = 'PostMan', collection = 'Messages')
            return True
        except e:
            return False

    def getMessages(self) -> list[dict[str, str]]:
        if self.server is None:
            self.initializeServer()

        msgs = list(map(lambda msg: {
                'content': msg['content'], 'author': msg['author']
            }, list(self.server.msgs.find())))
        return msgs

    def initializeServer(self, servername: str, username: str = None):
        if username is not None:
            self.username = username
        self.server = MongoServer(uri=servername, database='PostMan', collection='Messages')

    def sendMessage(self, msg: dict[str, str]):
        msg['time_of_arrival'] = arrow.utcnow()
        msg['status'] = Status.Unread
        self.server.add(Message.from_dict(msg))

class PostMan:
    def __init__(self):
        with open('ui/main.html', 'r') as f:
            html = f.read()
            api = PrimitiveApi()
            webview.create_window('PostMan', html = html, js_api=api)
            webview.start(debug=True)