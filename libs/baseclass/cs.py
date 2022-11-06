from kivy.uix.screenmanager import Screen
from Modules.db import cs
from ..Widget.Listitem import ListItemWithIcon





list_color= "white" #color of  text in notes screens .
class Cs_notes(Screen):
	
	def add_list_items(self):
		"""method to add notes in list from in cs_notes"""
		for i in range(len(cs)):
			self.ids.Mathlist.add_widget(ListItemWithIcon(icon="file-pdf",text=cs[i],main_color=list_color))

	def on_enter(self):
		"""on enter. use to generate the notes list on entering the screen"""
		
		self.add_list_items()
	
	def on_leave(self):
		"""on leave. use to reomve the notes list on leaving the screen"""
		
		self.ids.Mathlist.clear_widgets()
