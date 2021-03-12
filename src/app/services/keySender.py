# from injector import inject
from pynput.keyboard import Controller, Key
from time import sleep


class KeySender:
    def __init__(self) -> None:
        self.keyboard = Controller()

    def sendESC(self, waitTime: float = 0) -> None:
        # sleep(0.1)
        print("wysyłam ESC")
        # sleep(waitTime)
        self.keyboard.press(Key.esc)
        self.keyboard.release(Key.esc)

    def sendWord(self, word: str, timeBeforeStart: float = 0) -> None:
        sleep(timeBeforeStart)
        print(f"wysyłam \"{word}\". (Po odczekaniu: {timeBeforeStart}).")
        for mark in word:
            self.keyboard.press(mark)
            self.keyboard.release(mark)
        self.sendEnter()
        # self.sendESC()

    def sendEnter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def sendAltTab(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
        self.keyboard.release(Key.alt_l)
