from kivy.app import App
#kivy.require("1.10.0")
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import NumericProperty, ListProperty, StringProperty, ObjectProperty, DictProperty
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button

from pubgAPI import PUBG_API
from fortniteAPI import Fortnite
from kivy.config import Config




Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '768')
Config.set('graphics', 'height', '800')
LabelBase.register(name='LuckiestGuy',fn_regular="LuckiestGuy.ttf")
LabelBase.register(name='HELR65W',fn_regular="HELR65W.ttf")


#
# Main Screen - recieve selection/call screen
#

class MainScreen(Screen):

    def pubg_selected(self, instance, value):
        if value == 'down':
            self.game = "pubg"
        else:
            self.game = "None"
    
    def fortnite_selected(self, instance, value):
        if value == 'down':
            self.game = "fortnite"
        else:
            self.game = "None"

    def csgo_selected(self, instance, value):
        if value == 'down':
            self.game = "csgo"
        else:
            self.game = "None"


#
# Fortnite Screen - api call/store/update
#

class FortniteScreen(Screen):
    rating_label = DictProperty(rebind=True)
    
    def __init__(self, **kwargs):
        super(FortniteScreen, self).__init__(**kwargs)
        self.rating_label = {"trnRating":"", 'score':'', 'top1': '', 'top10':'','top25':'', 'kd':'', 'winRatio':'', 'matches':'', 'kills':'', 'kpg':'', 'scorePerMatch':''}

    def player_rating(self,name):
        get_stats_fortnite1 = Fortnite()
        get_stats_fortnite1.playerGet(name)
        self.rating_label = get_stats_fortnite1.playerStats()
        print("Called Fortnite Class--> " + str(self.rating_label))

    def get_rating(self):
        print("Called Get_Rating -->" + str(self.rating_label))
        return self.rating_label


#
# CSGO Screen - In progress
#

class CsgoScreen(Screen):
    pass


#
# PUBG Screen - Call api/store/update
#


class PubgScreen(Screen):
    pubg_label = DictProperty(rebind=True)

    def __init__(self, **kwargs):
        super(PubgScreen, self).__init__(**kwargs)
        self.pubg_label = {"boosts": 0,
          "dailyKills": 0,
          "damageDealt": 0,
          "days": 0,
          "headshotKills": 0,
          "heals": 0,
          "kills": 0,
          "longestKill": 0,
          "longestTimeSurvived": 0,
          "losses": 0,
          "maxKillStreaks": 0,
          "mostSurvivalTime": 0,
          "revives": 0,
          "rideDistance": 0,
          "roadKills": 0,
          "roundMostKills": 0,
          "roundsPlayed": 0,
          "timeSurvived": 0,
          "top10s": 0,
          "vehicleDestroys": 0,
          "weaponsAcquired": 0,
          "weeklyKills": 0,
          "wins": 0}

    def player_rating(self, name):
        get_stats_pubg = PUBG_API()
        get_stats_pubg.getPlayer(name)
        self.pubg_label = get_stats_pubg.get_data()
        print("Called PUBG Screen Class-->" + str(self.pubg_label))

    def get_rating(self):
        print("Called PUBG get rating ---")
        return self.pubg_label




class ScreenManagement(ScreenManager):
    main_screen = ObjectProperty(None)
    fortnite_screen = ObjectProperty(None)
    csgo_screen = ObjectProperty(None)
    pubg_screen = ObjectProperty(None)




MainFile = Builder.load_file("main.kv")




class MainApp(App):

    def show_popup(self):
        content = BoxLayout(orientation= "vertical")
        label=Label(text= 'CSGO Player Stats are still in development')
        content.add_widget(label)
        self.popup = Popup(title='Model is Running.', size_hint=(.400, .350), content=content, auto_dismiss=True)
        self.popup.open()

    def process_button_click(self):
        self.show_popup()

    def build(self):
        return MainFile




if __name__ == "__main__":
    MainApp().run()


# TODO: CSGO Code - api/labels/screen etc.
# TODO: Clean the code - Adjust variable names / etc.