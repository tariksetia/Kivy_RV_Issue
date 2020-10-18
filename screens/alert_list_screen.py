from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.resources import resource_add_path
from kivy.core.window import Window
from dataclasses import dataclass
from kivy.animation import Animation
import os, uuid
from kivy.clock import Clock



KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)
Builder.load_file('alert_list_screen.kv')


@dataclass
class Data:
    sent: str
    sender: str
    expires: str
    long_text: str
    language: str
    short_text: str
    category: str
    event:str
    area_desc: str
    alert_id: str
    status:str


    @property
    def to_dict(self):
        return self.__dict__


class FlatButton(Button):
    pass

class FieldName(Label):
    pass

class FieldValue(Label):
    pass

class FieldValueWrappable(Label):
    pass

class AlertListBox(BoxLayout):
    pass

class BorderLabel(Label):
    pass

class BackgroundLabel(Label):
    background_color = StringProperty("#fc960c")


class AlertCard(GridLayout):

    alert = ObjectProperty()
    card_state = StringProperty()
    screen_manager = ObjectProperty()
    closing_time = NumericProperty(0.2)
    background_color = StringProperty("#FFFFFF")
    screen_manager = ObjectProperty()

    sent = StringProperty()
    sender = StringProperty()
    expires = StringProperty()
    long_text = StringProperty()
    language = StringProperty()
    short_text = StringProperty()
    category = StringProperty()
    event = StringProperty()
    area_desc = StringProperty()
    alert_id = StringProperty()
    status = StringProperty()
    spanish_toggle_state = StringProperty('normal')
    english_toggle_state = StringProperty('down')


    def show_spanish(self):
        idx = self.parent.get_view_index_at(self.center)
        data = self.parent.parent.data
        self.language = "Spanish"
        data[idx]['language'] = 'Spanish'
        
    
    def show_english(self):
        idx = self.parent.get_view_index_at(self.center)
        data = self.parent.parent.data
        self.language = "English"
        data[idx]['language'] = 'English'

class Card(BoxLayout):

    alert = ObjectProperty()
    card_state = StringProperty()
    screen_manager = ObjectProperty()
    closing_time = NumericProperty(0.2)
    background_color = StringProperty("#FFFFFF")
    screen_manager = ObjectProperty()

    sent = StringProperty()
    sender = StringProperty()
    expires = StringProperty()
    long_text = StringProperty()
    language = StringProperty()
    short_text = StringProperty()
    category = StringProperty()
    event = StringProperty()
    area_desc = StringProperty()
    alert_id = StringProperty()
    status = StringProperty()
    spanish_toggle_state = StringProperty('normal')
    english_toggle_state = StringProperty('down')


    def show_spanish(self):
        idx = self.parent.get_view_index_at(self.center)
        data = self.parent.parent.data
        self.language = "Spanish"
        data[idx]['language'] = 'Spanish'
        
    
    def show_english(self):
        idx = self.parent.get_view_index_at(self.center)
        data = self.parent.parent.data
        self.language = "English"
        data[idx]['language'] = 'English'



class AlertListScreen(Screen):
    main_screen_manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        Clock.schedule_once(self.load_data,0)
        pass


    def load_data(self, dt):
        alerts = [Data(**s) for s in samples][:2]
        data = []
        for alert in alerts:
            row = {
                'alert': alert,
                'sent': alert.sent,
                'sender': alert.sender,
                'expires': alert.expires,
                'long_text': alert.long_text,
                'language': "English | en-US", 
                'short_text': alert.short_text,
                'category': alert.category,
                'event': alert.event,
                'area_desc': alert.area_desc ,
                'alert_id': alert.alert_id,
                'status': "Acutal public alert".upper(),
                'screen_manager': self.main_screen_manager,
                'english_toggle_state': 'down',
                'spanish_toggle_state': 'normal'
            }
            data.append(row)
        self.ids.alert_list_view.data = data 



samples =[
    {
        'sent' : "Mickey Mouse",
        'sender' : "Mickey Mouse",
        'expires' : "12/12/2020 11:11:11",
        'long_text' : "Mickey Mouse" * 10,
        'language' : "English | en-US" ,
        'short_text' : "Mickey   " * 10,
        'category' : "HAZMAT",
        'event' : "Election",
        'area_desc' : "Mickey Mouse" ,
        'alert_id' : "1800-US-ELECTION",
        'status' : "Acutal public alert".upper(),
    },

    {
        'sent' : "Donald Duck",
        'sender' : "Donald Duck",
        'expires' : "12/12/2020 11:11:11",
        'long_text' : "Donald Duck" * 20,
        'language' : "English | en-US" ,
        'short_text' : "Donald   " * 10,
        'category' : "HAZMAT",
        'event' : "Election",
        'area_desc' : "Donald Duck" ,
        'alert_id' : "1800-US-ELECTION",
        'status' : "Acutal public alert".upper(),
    },

    {
        'sent' : "Uncle Scrooge",
        'sender' : "Uncle Scrooge",
        'expires' : "12/12/2020 11:11:11",
        'long_text' : "UncleScrooge" * 30,
        'language' : "English | en-US" ,
        'short_text' : "Scrooge  " * 10,
        'category' : "HAZMAT",
        'event' : "Election",
        'area_desc' : "Uncle Scrooge",
        'alert_id' : "1800-US-ELECTION",
        'status' : "Acutal public alert".upper(),
    },
]


if __name__ == "__main__":
    Window.clearcolor = (1, 1, 1, 1)

    AlertsBoardApp().run()