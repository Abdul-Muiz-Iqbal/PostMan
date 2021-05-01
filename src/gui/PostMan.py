import PySimpleGUI as sg
from base import MongoServer
from utils import Message, Status
import arrow, threading

class PostMan:
    """Please Don't Roast My Gui Code."""

    def __init__(self) -> None:
        self.window = sg.Window('PostMan', self.layout())
        self.mongo = None

    def layout(self):
        return [
            [sg.Column([
                [sg.Text("Enter Your UserName For This Session:")],
                [sg.Input(key='username')],
                [sg.Text("Enter A Public Server Url:")],
                [sg.Input(key='server_uri')],
                [sg.Button('Join')]
            ], key='-COL1-')],
            [sg.Column([
                [sg.Text('Server Chatting', size=(40, 1))],
                [sg.Output(size=(110, 30), font=('Helvetica 10'), key='-OUTPUT-')],
                [
                    sg.MLine(size=(60, 5), enter_submits=True, key='-QUERY-', do_not_clear=False),
                    sg.Button('SEND', bind_return_key=True)
                ]
            ], visible=False, key='-COL2-')]
        ]

    def loop(self):
        firsttime = True
        displayed = []

        def look_for_msgs():
            while True:
                if self.mongo:
                    # Default, Update with new msgs
                    for msg in self.mongo.msgs.find():
                        if msg['_id'] not in displayed:
                            displayed.append(msg['_id'])
                            print(f"{msg['author']} :: {msg['content']}")
            
                    self.window.Refresh()
        t = threading.Thread( target=look_for_msgs )
        t.start()

        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break

            if event == 'Join':
                self.username = values['username']
                self.mongo = MongoServer(
                    values['server_uri'],
                    'PostMan', 'Messages'
                )
                self.window['-COL1-'].update(visible=False)
                self.window['-COL2-'].update(visible=True)

                if firsttime:
                    print('')
                    firsttime = False
            
            if event == 'SEND':
                query: str = values['-QUERY-'].rstrip()
                msg = Message(
                    content = query,
                    author = self.username,
                    time_of_arrival = arrow.utcnow(),
                    status = Status.Unread
                )
                self.mongo.add(msg)

                

        self.window.close()
