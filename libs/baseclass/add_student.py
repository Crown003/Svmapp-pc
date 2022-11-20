from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from os import getcwd as cwd
import sys
sys.path.insert(0,cwd()+"//")
from Modules.db import collection
from kivymd.uix.picker import MDDatePicker

class Add_Student(Screen):
	def on_save(self, instance, value, date_range):
		self.dob= value
	def on_cancel(self, instance, value):
		'''Events called when the "CANCEL" dialog box button is clicked.'''
		self.date.dilaog.dismiss()
	def show_date_picker(self):
	    self.date_dialog = MDDatePicker(title_input="Enter your Date of Birth",title="Select Your DOB",max_year=2030)
	    self.date_dialog.bind(on_save=self.on_save,on_cancel=self.on_cancel)
	    self.date_dialog.open()
	def add_student_from_teacher(self,Enroll,Nam,Clas,Sec,Ph,Email):
		"""this method is used to create a new student profile from teachers portal"""
		print(Enroll,"self.dob",Nam,Clas,Sec,Ph,Email)
		try:
			collection.insert_one({"Enrollment":Enroll,"DOB":str(self.dob),"Password":Ph,"Email":Email,"Username":Nam,"Class":Clas,"Sec":Sec,"Phone":Ph,"Role":'Student',"totalPresentDays":60,"UnitOneMarks":[0,0,0,0,0],"UnitTwoMarks":[0,0,0,0,0],"UnitThreeMarks":[0,0,0,0,0]})
			toast("Student added Successfully.")
			self.ids.StuEnrollmentNumber.text = ""
			self.ids.StuName.text = ""
			self.ids.StuClass.text = ""
			self.ids.StuSection.text = ""
			self.ids.StuPhone.text = ""
		except Exception as e:
			print(e)
			toast("Error ! unable to add student.")
	
