
if __name__ == "__main__":
    from screens.main_screen import IPASApp
    from utils import set_windows_config
    set_windows_config()
    IPASApp(db=None, warn_processor=None).run()
