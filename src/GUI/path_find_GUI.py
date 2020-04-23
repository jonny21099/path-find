import kivy
kivy.require('1.11.1') 

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class LoginScreen(Screen):
	pass

class MainActivity(Screen):
	pass

class WindowManager(ScreenManager):
	pass

interface = Builder.load_file("pathfind.kv")

class PathFinder(App):
	def build(self):
		return interface

if __name__ == '__main__':
	PathFinder().run()