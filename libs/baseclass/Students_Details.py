from kivy.uix.screenmanager import Screen
from Modules.db import collection
from kivymd.uix.list import OneLineListItem
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from PIL import Image
import io


class Student_Details(Screen):
	def all_cls_students_list(self):
		with open("Modules//loginfo.txt","r+") as f:
			data_new =  f.read().split(",")
			a = collection.find({"Role":"Student","Class":data_new[3][:2]})
		self.k = []
		for items in a:
			n = list([items["Enrollment"],items["Username"],items["Class"],items["Sec"]])
			self.k.append(n)
	def show_data(self):
		self.ids.grid.add_widget(OneLineListItem(text="Enmt no.   Name   Class   Sec",font_style="H5",theme_text_color="Custom",text_color=[1,0,0,.85]))
		for i in range(len(self.k)):
			z = len(self.k[i][1])//3 if len(self.k[i][1]) > 10 else len(self.k[i][1]) #slicing the name
			self.ids.grid.add_widget(OneLineList(text=f"{self.k[i][0]}   {self.k[i][1][:z].replace(' ','')}   {self.k[i][2]}   {self.k[i][3]}",theme_text_color="Custom",text_color=[0,0,0,1]))
	def on_enter(self):
		self.all_cls_students_list()
		self.show_data()
class OneLineList(OneLineListItem):
	def students_details_sheet(self,data):
		a = data.split()
		with open("students.txt","w+") as f:
			f.write(f"{a[0]},{a[1]},{a[2]},{a[3]}")
		self.dialog = MDDialog(title="Student Details:",type="custom",content_cls= StudentDialogbox())
		self.dialog.open()
class StudentDialogbox(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	def get_Profile_image(self,enrollment_no="",path="./Student.png"):
		a = ""
		image = collection.find_one({"Enrollment":enrollment_no})
		try:
			pil_img = Image.open(io.BytesIO(image['ProfileImage']))
			print("here:  ",pil_img)
			a = "updated"
			profile_path = path
			pil_img.save(profile_path)
		except:
			print("profile image not updated.")
			a = ""
		return a
	def update_values(self):
		with open("students.txt","r+") as f:
			self.data = f.read().split(",")
		try:
			main_data = collection.find_one({"Enrollment":self.data[0]})
			self.ids.Enroll_field.text = main_data["Enrollment"]
			self.ids.Name_field.text = main_data["Username"]
			self.ids.Class_field.text = main_data["Class"]+main_data["Sec"]
			self.ids.Email_field.text = main_data["Email"]
			self.ids.Phone_field.text = main_data["Phone"]
			status = self.get_Profile_image(self.data[0],"./Student.png")
			if status != "updated":
				self.ids.student_img.source = "./noprofile.png"
			else:
				self.ids.student_img.source = "./Student.png"
			self.ids.student_img.reload()
			self.ids.image_label.text = ""
		except Exception as e:
			print(e)