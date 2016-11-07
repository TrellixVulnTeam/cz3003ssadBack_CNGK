from threading import Timer, Thread, Event
from datetime import datetime
import requests


class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def printer():
    link = "http://127.0.0.1:8000/email/"
    f = requests.get(link)
    print('Status: ' + str(f.status_code))
    print('Text:')
    print(f.text)
    print('Now: ' + str(datetime.now()))

t = perpetualTimer(5, printer)
t.start()
