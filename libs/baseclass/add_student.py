from kivy.uix.screenmanager import Screen
from Modules.db import collection
from kivymd.toast import toast
import sys
sys.path.insert(0,"/storage/emulated/0/MyApp/")

class Add_Student(Screen):
	def add_student_from_teacher(self,Enroll,Nam,Clas,Sec,Ph):
		#this method is used to create a new student profile from teachers portal"""
		try:
			collection.insert_one({"Enrollment":Enroll,"Password":Ph,"Email":"","Username":Nam,"Class":Clas,"Sec":Sec,"Phone":Ph,"Role":'Student'})
			toast("Student added Successfully.")
			#self.root.get_screen("Add_Student").ids.StuEnrollmentNumber.text = ""
#			self.root.get_screen("Add_Student").ids.StuName.text = ""
#			self.root.get_screen("Add_Student").ids.StuClass.text = ""
#			self.root.get_screen("Add_Student").ids.StuSection.text = ""
#			self.root.get_screen("Add_Student").ids.StuPhone.text = ""
			self.ids.StuEnrollmentNumber.text = ""
			self.ids.StuName.text = ""
			self.ids.StuClass.text = ""
			self.ids.StuSection.text = ""
			self.ids.StuPhone.text = ""
		except Exception as e:
			print(e)
			toast("Error ! unable to add student.")
	
