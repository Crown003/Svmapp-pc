from kivy.uix.screenmanager import Screen
from Modules.db import c
from ..Widget.Listitem import ListItemWithIcon





list_color= "white" 
class Chemistry_notes(Screen):
	def add_list_items(self):
		for i in range(len(c)):
			self.ids.Mathlist.add_widget(ListItemWithIcon(icon="file-pdf",text=c[i],main_color=list_color))

	def on_enter(self):
		self.add_list_items()
	def on_leave(self):
		self.ids.Mathlist.clear_widgets()