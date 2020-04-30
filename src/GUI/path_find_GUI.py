import kivy
kivy.require('1.11.1') 

import sqlite3
from kivy.config import Config
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

#connects to the sqlite3 database stored as users.db in the local storage
conn = sqlite3.connect("users.db")
c = conn.cursor()

#window is not sizable, everything is fixed size
Config.set("graphics", "resizable", False)


#this will be the screen that deals with path finding interactions
class MainActivity(Screen):
	userInput = BoxLayout(orientation="vertical")
	label = Label(text = "What size should the grid be? (numbers only)")
	userInput.add_widget(label)

	sizeInput = BoxLayout(orientation="horizontal")
	emptyLabel = Label(text = "")
	sizeInput.add_widget(emptyLabel)
	sizeInput1 = TextInput(multiline = False, padding = (28,12))
	sizeInput1.input_filter = "int"
	sizeInput.add_widget(sizeInput1)

	xLabel = Label(text = " x ")
	sizeInput.add_widget(xLabel)
	sizeInput2 = TextInput(multiline = False, padding = (28,12))
	sizeInput2.input_filter = "int"
	sizeInput.add_widget(sizeInput2)
	emptyLabel = Label(text = "")
	sizeInput.add_widget(emptyLabel)


	userInput.add_widget(sizeInput)

	popupWindow = Popup(title = "Works", content = userInput, size_hint = (None, None), size = (400, 150), auto_dismiss = False)



#window manager deals with the transitino between the two screens
class WindowManager(ScreenManager):
	pass

#using two different screens, the login screen and the mainactivity
class LoginScreen(Screen):
	username = ObjectProperty(None)
	password = ObjectProperty(None)

	#register button, handles all checks for database error
	def RegisterBtn(self):
		c.execute("SELECT * FROM users WHERE username = ?",(self.username.text,))
		regcheck = c.fetchall()
		if (len(regcheck) == 0):
			c.execute("INSERT INTO users VALUES (?, ?)",(self.username.text, self.password.text))
			conn.commit()
			prompt = "Success"
			message = "Successfully registered!"
		
		else:
			prompt = "Failed"
			message = "Username already exists!"

		#create content for the popup
		registerErrorPopup = BoxLayout(orientation="vertical")
		label = Label(text = message)
		registerErrorPopup.add_widget(label)
		popupWindow = Popup(title = prompt, content = registerErrorPopup, size_hint = (None, None), size = (400, 150), auto_dismiss = False)
		registerErrorPopup.add_widget(Button(text="ok", on_press = popupWindow.dismiss, size_hint = (0.2, 0.4), pos_hint = {"center_x": 0.5,"y": 0.1}))
		popupWindow.open()

	#login button, handles all chekcs for database error
	def LoginBtn(self):
		c.execute("SELECT * FROM users WHERE username = ?", (self.username.text,))
		logincheck = c.fetchall()
		#check if username exists
		if(len(logincheck) == 0):
			prompt = "Error"
			loginErrorPopup = BoxLayout(orientation = "vertical")
			label = Label(text = "This account is not registered!")
			loginErrorPopup.add_widget(label)
			popupWindow = Popup(title = prompt, content = loginErrorPopup, size_hint = (None, None), size = (400, 150), auto_dismiss = False)
			loginErrorPopup.add_widget(Button(text="ok", on_press = popupWindow.dismiss, size_hint = (0.2, 0.4), pos_hint = {"center_x": 0.5,"y": 0.1}))
			popupWindow.open()

		#check if password is correct
		elif(len(logincheck) == 1 and logincheck[0][1] != self.password.text):
			prompt = "Error"
			loginErrorPopup = BoxLayout(orientation = "vertical")
			label = Label(text = "The username or password is incorrect!")
			popupWindow = Popup(title = prompt, content = loginErrorPopup, size_hint = (None, None), size = (400, 150), auto_dismiss = False)
			loginErrorPopup.add_widget(Button(text="ok", on_press = popupWindow.dismiss, size_hint = (0.2, 0.4), pos_hint = {"center_x": 0.5,"y": 0.1}))
			popupWindow.open()

		#if all checks are satisfied switch into the mainactivity
		else:
			MainActivity.popupWindow.open()
			self.manager.current = "path_finding_interaction"

#loading in the pathfind.kv file
interface = Builder.load_file("pathfind.kv")

class PathFinder(App):
	def build(self):
		return interface

if __name__ == '__main__':
	PathFinder().run()