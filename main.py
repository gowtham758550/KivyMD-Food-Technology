from kivymd.app import MDApp
from webbrowser import open

				
class FoodTechnologyApp(MDApp):
	def build(self):
		icon = 'icon.svg'
		self.theme_cls.primary_palette = "Red"
		
	def open_link(self, url):
		open(url)
				
FoodTechnologyApp().run()