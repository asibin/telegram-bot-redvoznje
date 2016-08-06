# Belgrade Public Transportation Bot

Belgrade public transportation telegram bot. 

This was a friday night project so it is not perfect in any way :)

Bot currently displays images of schedules of buses, night buses, minibuses, 
trams, trolleys and Belgrade trains (BG-Voz) from an external service.

## NOTE
If you want to use this bot on Telegram all you need to do is add `@BGRedVoznje` bot
from your telegram application, you don't need to follow these instructions.

Instructions below are for people who want to self host bot under different name.

## Instalation
Install requirements inside virtualenv:
```python
pip install -r requirements.txt 
```

## Setup
Rename `settings-example.py` to `settings.py` and insert your token in TOKEN variable.
You can get your token by contacting `@BotFather` on telegram and running `/newbot` command.

Start your bot with `python telegram-bot.py`.

## Usage and Examples
Type `/` and bot will offer available commands.

For example, write `/bus 53` to get a bus schedule for bus line 53. Please note: currently
as this app does not differentiate between buses, minibuses, trolleys and trams all of these
"categories" use `bus` keyword.

Ti get train schedule you can use `/train <first_station>`, currently only two available
arguments are `pancevacki` and `batajnica`, so in order to get train schedule you can write:
`/train pancevacki` to get schedule for trains starting from `Pancevacki Most` station.

## Data Information
Data is taken from the third party service. Accuracy of said data cannot be guaranteed. 

## TODO
* Add more commands
* Parse available bus numbers from official website
* Stop using external service
* Separate different directions
