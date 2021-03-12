# from config import setProjectPath  # type: ignore
# setProjectPath()
from injector import Injector
from src.app.appRunner import App


if __name__ == "__main__":
    iocContainer = Injector()
    app = iocContainer.get(App)

    # app = App()
    app.run()
