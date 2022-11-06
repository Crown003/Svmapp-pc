from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from Modules.db import collection
import requests

#this code is managing the whole login validation work.
class LoginPage(Screen):
	def loginUser(self,name,password):
		if name.text == "" or password.text == "":
			toast(text="Please enter some valid credentials",gravity=80)
		else:	
			try:
				requests.get(url="https://google.com",timeout=5)
				self.user_obj = collection.find_one({"$or": [{"Enrollment":name.text,"Password":password.text},{"Username":name.text,"Password":password.text}]})
				if self.user_obj != None :
					User_obj = self.user_obj
					if self.user_obj["Username"] != "" and self.user_obj["Role"].upper()== "STUDENT" :
						Enrollment_no = self.user_obj["Enrollment"]
						User = self.user_obj["Username"]
						Class = self.user_obj["Class"]
						Sec = self.user_obj["Sec"]
						Phone = self.user_obj["Phone"]
						Email = self.user_obj["Email"]
						Role = self.user_obj["Role"]
						PresentDays = self.user_obj["totalPresentDays"]
						UTO = self.user_obj["UnitOneMarks"]
						UTT = self.user_obj["UnitTwoMarks"]
						UTTh = self.user_obj["UnitThreeMarks"]
						self.manager.transition.direction = "left"
						self.manager.current = "Home"
						with open("Modules//loginfo.txt","w+") as f:
							f.write(f"logged,{Role},{User},{Class},{Sec},{Phone},{Email},{Enrollment_no},{PresentDays}")	
						with open("Modules//numbers.txt","w+") as k:
							k.write(f"{UTO}-{UTT}-{UTTh}")				
					elif self.user_obj["Username"] != "" and self.user_obj["Role"].upper()== "TEACHER":
						User = self.user_obj["Username"]
						Class = self.user_obj["Class"]
						Role = self.user_obj["Role"]
						self.manager.current = "Teachers_interface"
						with open("Modules//loginfo.txt","w+") as f:
							f.write(f"logged,{Role},{User},{Class}")
					else:
						pass
				else:
					toast("No user found with given credentials.")
			except Exception as e:
				if e == "HTTPSConnectionPool(host='google.com', port=443): Read timed out. (read timeout=5)":
					toast(text="Please check your internet connection !!",gravity=80)
				else:
					print("from login: ",e)
					toast(text="Oops ! something went wrong please check your conection or try again later.")
