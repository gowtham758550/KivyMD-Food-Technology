from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from webbrowser import open
				
class FoodTechnologyApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Red"
		
	def open_link(self, url):
		open(url)
				
FoodTechnologyApp().run()