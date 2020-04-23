import kivy
kivy.require('1.11.1') 

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class login_screen(Screen):
	# username = ObjectProperty(None)
	# password = ObjectProperty(None)

	# def btn(self):
		
	# 	self.username.text = ""
	# 	self.password.text = ""
	pass

class main_activity(Screen):
	pass

class WindowManager(ScreenManager):
	pass

GUI = Builder.load_file("pathfind.kv")

class PathFinder(App):
    def build(self):
        return GUI


if __name__ == '__main__':
    PathFinder().run()