from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser
from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        filepath = f'files/{current_time}.png'
        self.ids.camera.export_to_png(filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath


class ImageScreen(Screen):
    def create_link(self):
        filepath = self.manager.current_screen.ids.img.source
        filesharer = FileSharer(filepath=filepath)
        url = filesharer.share()
        self.ids.label.text = url

    def copy_link(self):
        url = self.ids.label.text
        Clipboard.copy(url)

    def open_link(self):
        url = self.ids.label.text
        webbrowser.open(url)


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
