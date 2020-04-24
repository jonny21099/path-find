import kivy
kivy.require('1.11.1') 

import sqlite3

from kivy.config import Config
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

#connects to the sqlite3 database stored as users.db in the local storage
conn = sqlite3.connect("users.db")
c = conn.cursor()

#window is not sizable, everything is fixed size
Config.set("graphics", "resizable", False)

#using two different screens, the login screen and the mainactivity
class LoginScreen(Screen):
	username = ObjectProperty(None)
	password = ObjectProperty(None)

	#register button, handles all checks for database error
	def RegisterBtn(self):
		c.execute("SELECT * FROM users WHERE username = ?",(self.username.text,))
		check = c.fetchall()
		if (len(check) == 0):
			c.execute("INSERT INTO users VALUES (?, ?)",(self.username.text, self.password.text))
			conn.commit()
			show = RegisterSuccessPopup()
			message = "Success"
		else:
			show = RegisterFailurePopup()
			message = "Failed"

		popupWindow = Popup(title = message, content = show, size_hint = (None, None), size = (400, 150), auto_dismiss = False)
		popupWindow.open()

	#login button, handles all checks for database error
# 	def LoginBtn(selfsqlite> select * from users
# ):
# 		pass

#this will be the screen that deals with path finding interactions
class MainActivity(Screen):
	pass

#window manager deals with the transitino between the two screens
class WindowManager(ScreenManager):
	pass

#popup for successfully registered
class RegisterSuccessPopup(FloatLayout):
	pass

#popup for registration failure
class RegisterFailurePopup(FloatLayout):
	pass

#loading in the pathfind.kv file
interface = Builder.load_file("pathfind.kv")

class PathFinder(App):
	def build(self):
		return interface

if __name__ == '__main__':
	PathFinder().run()