from kivy.uix.screenmanager import Screen
from Modules.db import cs
from ..Widget.Listitem import ListItemWithIcon





list_color= "white" #color of  text in notes screens .
class Cs_notes(Screen):
	
	def check_file_exist(self,file):
			#this method check the file existance"""
			from os.path import exists
			from os import getcwd as cwd
			a = exists(cwd()+"/Notes/"+ file + ".pdf")
			return a

	def add_list_items(self):
		for i in range(len(cs)):
			if cs[i]:
				icon="file-pdf"
				color= 1,0,0,1
				if self.check_file_exist(cs[i]) == True:
					icon="check-underline"
					color = 0,1,0,1
				self.ids.Mathlist.add_widget(ListItemWithIcon(text=cs[i],icon=icon,theme_text_color="Custom",text_color=color))

	def on_enter(self):
		"""on enter. use to generate the notes list on entering the screen"""
		
		self.add_list_items()
	
	def on_leave(self):
		"""on leave. use to reomve the notes list on leaving the screen"""
		
		self.ids.Mathlist.clear_widgets()
