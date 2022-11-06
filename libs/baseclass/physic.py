from kivy.uix.screenmanager import Screen
from Modules.db import p
from ..Widget.Listitem import ListItemWithIcon


list_color= "white" 
class Physics_notes(Screen):
	def check_file_exist(self,file):
			#this method check the file existance"""
			from os.path import exists
			from os import getcwd as cwd
			a = exists(cwd()+"/Notes/"+ file + ".pdf")
			return a

	def add_list_items(self):
		for i in range(len(p)):
			if p[i]:
				icon="file-pdf"
				color= 1,0,0,1
				if self.check_file_exist(p[i]) == True:
					icon="check-underline"
					color = 0,1,0,1
					print("i came here")
				self.ids.Mathlist.add_widget(ListItemWithIcon(text=p[i],icon=icon,theme_text_color="Custom",text_color=color))



	def on_enter(self):
		self.add_list_items()
	def on_leave(self):
		self.ids.Mathlist.clear_widgets()