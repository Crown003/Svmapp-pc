from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from os import getcwd as cwd
import sys
sys.path.insert(0,cwd()+"//")
from Modules.db import collection

class Add_Student(Screen):
	def add_student_from_teacher(self,Enroll,Nam,Clas,Sec,Ph):
		"""this method is used to create a new student profile from teachers portal"""
		try:
			collection.insert_one({"Enrollment":Enroll,"Password":Ph,"Email":"","Username":Nam,"Class":Clas,"Sec":Sec,"Phone":Ph,"Role":'Student',"totalPresentDays":60,"UnitOneMarks":{},"UnitTwoMarks":[],"UnitThreeMarks":[],})
			toast("Student added Successfully.")
			self.ids.StuEnrollmentNumber.text = ""
			self.ids.StuName.text = ""
			self.ids.StuClass.text = ""
			self.ids.StuSection.text = ""
			self.ids.StuPhone.text = ""
		except Exception as e:
			print(e)
			toast("Error ! unable to add student.")
	
