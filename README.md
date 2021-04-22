# Covid19ReliefBot
A Bot for getting Information on Relief Facilities for Covid 19 Patients and Easily Find Services in Emergency.

The Bot is completely Open Source and you can download the Source Code and use it for fair purposes.

#### Inspired by [covid19-twitter.in](https://www.covid19-twitter.in/) - [Github](https://github.com/umanghome/twitter-search-covid19/)

## How to Setup the Bot
* Download the Source Code.
* Make Sure you have Python (3.7 or Newer) Installed on your Device. If not, Install it from the [Official Python Website](https://www.python.org/downloads/).
* Make a Bot Application. (More Info at this [Website](https://discordpy.readthedocs.io/en/stable/discord.html))
* In the Credentials file ([credentials.json](./bot/data/credentials.json)), fill in the required credentials.
  * In `token`, fill in the Bot's Token you made in Step 3rd.
  * In `prefix`, fill in the Prefix of your Choice for your Bot.
* Example:
```json
{
    "token": "abcdefghijklmnopqrstuvwxyz1234567890",
    "prefix": "!"
}
```
* Run the [launcher.py](./launcher.py) File.


* The Bot should install all Dependencies by Itself if all the Python and PIP Settings are configured Properly on your Device.
* In case some error occurs, install the dependencies listed in the [requirements.txt](./requirements.txt) file manually and then go to [launcher.py](./launcher.py) File and comment out 2nd (`os.system("pip3 install -r requirements.txt")`) line and again run the File.

## Some Resouces
In the Hard Times, You should help people whosoever is in the Need of. Unavailability of Resources is getting a Big Issue.
I added some resources I can find in the file [resources.txt](./resources.txt) and I'll update them as I will find more.

These are not used in the Bot, but for general Help. You can share them with the needy and this may help them.