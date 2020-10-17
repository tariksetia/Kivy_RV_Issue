
import os, time, random, hashlib
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.resources import resource_add_path
from .alert_list_screen import AlertListScreen

KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)

Builder.load_file('main_screen_manager.kv')


def get_hash(xml_str):
    h = hashlib.md5(xml_str.encode())
    return h.hexdigest()


class MainScreenManager(ScreenManager):

    def show_dashboard(self):
        self.current = 'screen_dashboard'
    
    def show_alert_list(self):
        self.current = 'screen_alert_list'
    
    def show_heartbeat_list(self):
        self.current = 'screen_hbeat_list'

    def show_alert_details(self, alert, screen=None):
        name = str(time.time())
        ads = AlertDetailScreen(name=name)
        ads.alert = alert
        ads.main_screen_manager = self
        if screen:
            ads.ids.AlertDetailScreenManager.current = screen
        self.add_widget(ads)
        self.current=name
    
    def process_cmac(self, xml):
        cmac = CMAC(xml)
        cmac.raw_hash = get_hash(xml)
        insert_alert(cmac)


class ScreenManagerApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
    ScreenManagerApp().run()