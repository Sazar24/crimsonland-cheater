## About

This app allows you to cheat in newest (today is 2021) Crimsonland "type'o'shooter" mode.
The cheating mechanism is that when you are loosing focus from game window (alt+tab, for example), it automatically shows menu.
But you are still able to see monsters names (which you need to type in, to shoot type)
This app allows you to shoot those monster 5 times per second, and take all the time you need to prepare the shot.
Just open crimsonland in windowed mode and start type'o'shooter mode.
Then start the app and follow instruction in app console/terminal.

Thanks to it, Im the first one who crossed the barrier of 100k points in Steam highscores.

### usage and shortcuts:

Bassicaly, you will have to type in each monster name.
But sometimes you can miss some, or they will be exceptionally strong/tough. Or you will want to go manual, to cheack is it really thats hard to try without ~~cheating~~ help.

Shortcut list (type in instead of monster name):

- "r" (yeap, just one letter. Monsters never have one-letter name) (R stands for (R)epeat) - repeat last given phrase (use on tough monsters)
- "w" ((W)ait) - go manual.
- alt+tab - use when u want to go back to "cheating mode", when u are in manual. You could use mouse for that too, of course, but thats just a waste of time.

## Requirements:

- NodeJS (recommended)
- Python3+ (with pip, of course)
- Windows (developed and tested on Windows 10)
- Crimsonland (buyyable on steam) in windowed mode

## Some technical stuff:

- This app uses key emits signals (some kind of user keypress simulation), to send text to game window (pythons pynput library)
- It works only on Windows, because its uses Windows PID (Process ID) to focus on game window - and I wasn't even bother about linux, sorry. Linux is not meant for games :P

## How to start

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
