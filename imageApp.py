# Import libraries of code
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass


class NobelWindow(Screen):
    pass


class PatchWindow(Screen):
    pass


class TrustyWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("theimageprog.kv")


# Inherit App class to MyApp class for use
# Window design file in theProg.kv file
class theImageProg(App):
    def build(self):
         return kv


# Run the App if the main program is starting it
if __name__ == "__main__":
    theImageProg().run()
