from injector import inject
from src.app.services.keySender import KeySender
from src.app.services.gameFocuser import GameFocuser


class App:
    @inject
    def __init__(self,
                 keySender: KeySender,
                 windowFocuser: GameFocuser
                 ):
        self.keySender = keySender
        self.windowFocuser = windowFocuser

    def run(self):
        print("The App has been started.")

        self._saveGamePid()
        self._waitForInput()

    def _saveGamePid(self) -> None:
        self.windowFocuser.getAppPID()

    def _startCheating(self) -> None:
        """ oszukujemy w grze Crimsonland, w trybie type'o'shooter"""
        pass

    def _waitForInput(self) -> None:
        phrase: str = ""
        print("waiting for user input")
        lastWord: str = ""
        exitPhrase: str = "exit()"

        while phrase != exitPhrase:
            print("Give me a phrase to send: ")
            phrase: str = input()
            self.windowFocuser.focusOnApp()
            self.keySender.sendESC()

            if phrase == exitPhrase:
                break

            if phrase == "w":
                """ start manual mode (use "alt+tab" to return to console) """
                self.keySender.sendWord("", 0.9)
            elif phrase != "r":
                """If command is other than "[R]epeat" type in given phrase 5 times """
                print(f"Phrase to send: {phrase}")
                self.keySender.sendWord(phrase, 0.9)
                for _ in range(0, 5):
                    self.keySender.sendWord(phrase, 0.1)
                lastWord = phrase
                self._focusOnConsole()
            elif phrase == "r":
                """ Repeat last phrase 5 times - use on big monsters"""
                print(f"Repeating last phrase: {lastWord}")
                self.keySender.sendWord(lastWord, 0.9)
                for _ in range(0, 5):
                    self.keySender.sendWord(lastWord, 0.1)
                self._focusOnConsole()

    def _focusOnConsole(self) -> None:
        self.keySender.sendESC()
        self.keySender.sendAltTab()
