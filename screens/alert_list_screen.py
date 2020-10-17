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
    lbl_category: str
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

    def __init__(self, **kwargs):
        self.card_state = 'closed'
        self.hidden_widgets = []
        Clock.schedule_once(self._populate_data,0)
        super().__init__(**kwargs)

    def _populate_data(self, dt):
        self.ids.sent.text = self.alert.sent
        self.ids.sender.text = self.alert.sender
        self.ids.expires.text = self.alert.expires
        self.ids.long_text.text = self.alert.long_text
        self.ids.language.text = "English | en-US" 
        self.ids.short_text.text = self.alert.short_text
        self.ids.category.text = self.alert.category
        self.ids.event.text = self.alert.event
        self.ids.area_desc.text = self.alert.area_desc
        self.ids.alert_id.text = self.alert.alert_id
        self.ids.lbl_category.text = self.alert.category
        self.ids.status.text = "Acutal public alert".upper()


class AlertListScreen(Screen):
    main_screen_manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        Clock.schedule_once(self.load_data,0)
        pass


    def load_data(self,dt):
        alerts = [ Data(**s) for s in samples]
        data = []
        for alert in alerts:
            row = {
                'alert': alert,
                'screen_manager': None
            }
            data.append(row)
        self.ids.alert_list_view.data = data   



samples =[
    {
        'sent' : "Mickey Mouse",
        'sender' : "Mickey Mouse",
        'expires' : "12/12/2020 11:11:11",
        'long_text' : "Mickey Mouse" * 30,
        'language' : "English | en-US" ,
        'short_text' : "Mickey   " * 10,
        'category' : "HAZMAT",
        'event' : "Election",
        'area_desc' : "Mickey Mouse" ,
        'alert_id' : "1800-US-ELECTION",
        'lbl_category' : "Safety",
        'status' : "Acutal public alert".upper(),
    },

    {
        'sent' : "Donald Duck",
        'sender' : "Donald Duck",
        'expires' : "12/12/2020 11:11:11",
        'long_text' : "Donald Duck" * 30,
        'language' : "English | en-US" ,
        'short_text' : "Donald   " * 10,
        'category' : "HAZMAT",
        'event' : "Election",
        'area_desc' : "Donald Duck" ,
        'alert_id' : "1800-US-ELECTION",
        'lbl_category' : "Safety",
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
        'lbl_category' : "Safety",
        'status' : "Acutal public alert".upper(),
    },
]


if __name__ == "__main__":
    Window.clearcolor = (1, 1, 1, 1)

    AlertsBoardApp().run()