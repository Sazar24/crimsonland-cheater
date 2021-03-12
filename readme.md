## About
This app allows you to cheat in newest (today is 2021) Crimsonland "type'o'shooter" mode.
The cheating mechanism is that when you are loosing focus from game window (alt+tab, for example), it automatically shows menu.
But you are still able to see monsters names (which you need to type in, to shoot type)
This app allows you to shoot those monster 5 times per second, and take all the time you need to prepare the shot.

Thanks to it, Im the first one who crossed the barrier of 100k points in Steam highscores.

## requirements:
- NodeJS (recommended)
- Python3+ (with pip, of course)
- Windows (developed and tested on Windows 10)
- Crimsonland (buyyable on steam) in windowed mode

## how to start
If you are familiar with nodeJS you should be able to find all information in package .json.
If you have nodeJS/npm installed in your system type in following commands:
```
npm i
npm run prebuild
venv\scripts\activate
pip install -r requirements.txt 
npm start
```

Otherwise, if you don't have nodeJS type in following commands:
```
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt 
python -m src.appStarter
```



## suggested vscode (json) settings:
already included in repo 
```
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "python.linting.enabled": true,
    "files.exclude": {
        // ".vscode/": true,
        "**/__pycache__": true,
        "**/__init__.py": true
    },
    "search.exclude": {
        "/src/_proofs": true,
    },
    "workbench.panel.defaultLocation": "bottom",
    "python.linting.pylintArgs": [
        // "--ignore-relative-beyond-top-level-dupas"
        "--max-line-length=220"
    ],
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--ignore=E501,E722,E125,W503,W504,E116",
        "--max-line-length=220"
    ],
    "python.formatting.autopep8Args": [
        "--max-line-length=220"
    ],
    // "python.jediEnabled": false,  // <--- z tym eksperymentować, kiedy nie działa...
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./src",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.unittestEnabled": true,
}

```