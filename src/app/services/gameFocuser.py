import psutil
from time import sleep
from pywinauto.application import Application


class GameFocuser:
    def __init__(self) -> None:
        self.processName = "Crimsonland"
        self.pid = None

    def getAppPID(self):
        for proc in psutil.process_iter():
            if self.processName in proc.name():
                self.pid = proc.pid
        if self.pid is None:
            raise Exception(f"Nie znaleziono uruchomionej aplikacji o nazwie: \"{self.processName}\".")
        else:
            print(f"Znalazłem PID aplikacji (\"{self.processName}\"): {self.pid}.")
            self.__connectToApp()

    def __connectToApp(self):
        try:
            # https://stackoverflow.com/questions/34110425/pywinauto-32-bit-userwarning
            self.app = Application(backend="uia").connect(process=self.pid)
            print("Podpiąłem się do aplikacji.")
        except:
            print("Coś jebło na etapie łączenia po PID aplikacji.")

    def focusOnApp(self, waitAfterFocus: float = 0.1):
        try:
            print("focusing on app...")
            self.app.top_window().set_focus()
            sleep(waitAfterFocus)
            print("success?")
        except:
            print("Coś jebło na etapie focusowania się na aplikacji")
