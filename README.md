# Game-Status-Tracker
## Python - game status tracker.

Python has excellent libraries and frameworks to work with, one of those libraries is Kivy. One of the problems I had as a Gamer, I always had to go through different websites to find my stats for a specific game and it got really repetative, dull and inconveniente. So I though why nobody creates an application which includes all the games stats?

### How does the program work

The program is really simple and I think easy to read. The API code - where the JSON request happen to a different games API, are stored in a different files:

* **_fortniteAPI.py_** 
* **_pubgAPI.py_** 

The main part and logic is stored in the main file:

* **_GameStatusTracker.py_**

Most of the code there is Python/ Kivy and logic to execute specific API calls.

If you run the main file, two windows will appear.

1. The "Logs" what happens in the background - which is why you can find `print()` statements in different places, that is just as assurance what gets called.
2. The main application window.

### Parts to Finish

- [x] PUBG API - Request|Recieve|Store|Use
- [x] Fortnite API - Request|Recieve|Store|Use
- [ ] CSGO API - Request|Recieve|Store|Use

### Project is not being continued
