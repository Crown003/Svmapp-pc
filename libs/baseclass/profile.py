from kivy.core.window import Window 
Window.softinput_mode = 'below_target'
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager
from Modules.db import collection
import io
from kivy import platform
from PIL import Image
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast
from os import getcwd as cwd
import json

if platform != "android":
	from plyer import filechooser

class Profile(Screen):	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		Window.bind(on_keyboard=self.events)
		self.manager_open = False
		self.file_manager = MDFileManager(exit_manager=self.exit_manager,select_path=self.select_path,preview=True,)
	def file_manager_open(self):
		if platform == "android":
			self.file_manager.show('/storage/emulated/0/')  # output manager to the screen
			self.manager_open = True	
		else:
			filechooser.open_file(on_selection= self.select_path)
		
	def select_path(self, path):
		if platform != "android":
			if path:
				with open(cwd() + r"\Modules\loginfo.json","r") as f:
					logged = json.loads(f.read())
					self.upload_image_details = [logged["userEnrollNum"],path[0]]
					self.upload_profile_photo(self.upload_image_details[0],self.upload_image_details[1])	
		else:	
			self.exit_manager(path)
	
	def exit_manager(self, *args):
		self.manager_open = False
		if args[0] != 1:
			with open(cwd() + r"/Modules/loginfo.json","r") as f:
				logged = json.loads(f.read())
				self.upload_image_details = [logged["userEnrollNum"],args[0]]
				self.upload_profile_photo(self.upload_image_details[0],self.upload_image_details[1])		
		else:
			toast("noting selected.")
		self.file_manager.close()
	def events(self, instance, keyboard, keycode, text, modifiers):
		if keyboard in (1001, 27):
			if self.manager_open:
				self.file_manager.back()
		return True
	def upload_profile_photo(self,enrollment,path):
		if path != "":
			im = Image.open(path)
			image_bytes = io.BytesIO()
			im.save(image_bytes, format='PNG')
			try:
				collection.update_one({"Enrollment":enrollment},{"$set":{'ProfileImage': image_bytes.getvalue()}})
				self.get_Profile_image(enrollment)
			except Exception as e:
				print(e)
		else:
			print("no profile photo selected by user.")
	def get_Profile_image(self,enrollment_no,path="./profile.png"):
		image = collection.find_one({"Enrollment":enrollment_no})
		pil_img = Image.open(io.BytesIO(image['ProfileImage']))
		profile_path = path
		pil_img.save(profile_path)
	def text_to_edit(self):
		self.ids.name_field.disabled = False
		self.ids.class_field.disabled = False
		self.ids.contact_field.disabled = False
		self.ids.email_field.disabled = False
		self.ids.name_field.icon_right = "pencil"
		self.ids.class_field.icon_right = "pencil"
		self.ids.contact_field.icon_right = "pencil"
		self.ids.email_field.icon_right = "pencil"
		self.ids.name_field.helper_text = "Your name"
		self.ids.class_field.helper_text = "Your class(write only integer. i.e 12)"
		self.ids.contact_field.helper_text= "Your phone no"
		self.ids.email_field.helper_text = "Your email"
		self.ids.camera.icon = "camera"
	def save_to_edit(self,Name,Class,Phone,Email):		
		self.ids.name_field.disabled = True
		self.ids.class_field.disabled = True
		self.ids.contact_field.disabled = True
		self.ids.email_field.disabled = True
		self.manager.get_screen("Home").ids.Nlabel.text = Name.text
		self.ids.camera.icon = ""
		self.ids.name_field.icon_right = ""
		self.ids.class_field.icon_right = ""
		self.ids.contact_field.icon_right = ""
		self.ids.email_field.icon_right = ""
		self.ids.name_field.text = Name.text
		self.ids.class_field.text = Class.text
		self.ids.contact_field.text = Phone.text	
		self.ids.email_field.text = Email.text
		if platform != "android":
			with open(cwd() + r"\Modules\loginfo.json","r") as f:
				data = json.loads(f.read())
		else:
			with open(cwd() + r"/Modules/loginfo.json","r") as f:
				data = json.loads(f.read())
		role = data["role"]
		sec = data["userSection"]
		phone = data["userPhone"]
		enrollment = data["userEnrollNum"]
		presentdays = int(data["userAttendence"])
		query = {"Enrollment":data["userEnrollNum"]}
		update_values = {"$set" : {"Username":Name.text,"Class":Class.text,"Phone":Phone.text,"Email":Email.text}}
		try:
			collection.update_one(query,update_values)
			User = Name.text
			Class = Class.text
			Phone = Phone.text
			Email = Email.text
			Sec = sec
			Role = role
			Phone = phone
			Enrollment_no = enrollment
			UnitOneMarks = data["userMarks"]["UnitOneMarks"]
			UnitTwoMarks = data["userMarks"]["UnitTwoMarks"]
			UnitThreeMarks = data["userMarks"]["UnitThreeMarks"]
			PresentDays = presentdays
			if platform != "android":
				with open(cwd() + r"\Modules\loginfo.txt","w+") as f:
					f.write('{"status":"%s","role": "%s","userName": "%s","userClass":"%s","userSection":"%s","userPhone":"%s","userEmail":"%s","userEnrollNum":"%s","userAttendence":"%s","userMarks":{"UnitOneMarks":[%s],"UnitTwoMarks":[%s],"UnitThreeMarks":[%s]}}'''%("logged","student",User,Class,Sec,Phone,Email,Enrollment_no,PresentDays,UnitOneMarks,UnitTwoMarks,UnitThreeMarks))	
			
			else:
				with open(cwd() + r"/Modules/loginfo.txt","w+") as f:
					f.write('{"status":"%s","role": "%s","userName": "%s","userClass":"%s","userSection":"%s","userPhone":"%s","userEmail":"%s","userEnrollNum":"%s","userAttendence":"%s","userMarks":{"UnitOneMarks":[%s],"UnitTwoMarks":[%s],"UnitThreeMarks":[%s]}}'''%("logged","student",User,Class,Sec,Phone,Email,Enrollment_no,PresentDays,UnitOneMarks,UnitTwoMarks,UnitThreeMarks))	
			
			toast(text="updated successfully")
			self.ids.pro_label.text = ""
		except Exception as e:
			print(e)
			a = Snackbar(text="Oops !  something wents wrong unable to update profile.")
			a.open()
			self.ids.pro_label.text = ""