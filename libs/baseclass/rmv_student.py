from kivy.uix.screenmanager import Screen
from Modules.db import collection
from kivymd.toast import toast
import multitasking
multitasking.set_max_threads(10)

class Rmv_Student(Screen):
	@multitasking.task
	def get_student_to_remove(self,stud_enroll):
		if stud_enroll:
			try:
				stud = collection.find_one({"Enrollment":stud_enroll})
				self.ids.loading_label.text = ""
				self.ids.name_stu.text = "Name: {0}".format(stud["Username"])
				self.ids.class_stu.text = "Class: {0}".format(stud["Class"])
				self.ids.email_stu.text = "Email: {0}".format(stud["Email"]) if stud["Email"] else "Email: *not updated" 
				self.ids.del_btn.opacity = 1
				self.ids.search_btn.disabled = False
			except Exception as e:
				print(e)
		else:
			toast(text="Please enter some valid data.")
			self.ids.loading_label.text = ""
			self.ids.search_btn.disabled = False
	@multitasking.task
	def del_student(self,stud_enroll):
		try:
			stud = collection.delete_one({"Enrollment":stud_enroll})
			toast(text="successfully deleted.",gravity=80)
			self.ids.StuEnrollmentNumber.text = ""
			self.ids.name_stu.text = ""
			self.ids.class_stu.text = ""
			self.ids.email_stu.text = ""
			self.ids.del_btn.opacity = 0
			self.ids.search_btn.disabled = False
		except Exception as e:
			print(e)
			