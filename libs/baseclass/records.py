from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from os import getcwd as cwd
#default data for graph of records screen.
unit_one_marks = [1,2,1,2,1]
unit_two_marks = [1,2,1,2,1]
unit_three_marks = [1,2,1,2,1]
total_school_working_day = 88
##### This whole code convert the string values to integer..(values extracted from db)   ########
with open(r"{0}/Modules/loginfo.txt".format(cwd()),"r+") as f:
	logged = f.read().split(",")
	student_attendance = logged[len(logged)-1]
with open(r"{0}/Modules/numbers.txt".format(cwd()),"r+") as f:
	a = f.read().split("-")
	b = a[0].replace("["," ")
	c = b.replace("]"," ").replace("'","").split(",")
	d = a[1].replace("["," ")
	e = d.replace("]"," ").replace("'","").split(",")
	f = a[2].replace("["," ")
	g = f.replace("]"," ").replace("'","").split(",")
	UTOmarks =[]
	UTTmarks =[]
	UTThmarks =[]
	if len(c) != 1:
		for item in c:
			UTOmarks.append(int(item.strip()))
	else:
		pass
	if len(e) != 1:
		for items in e:
			UTTmarks.append(int(items.strip()))
	if len(g) != 1:
		for itemss in g:
			UTThmarks.append(int(itemss.strip()))
	else:
		pass
	
###############
	if not UTOmarks:	
		unit_one_marks = [1,2,1,2,1]
	else:
		unit_one_marks =UTOmarks
	if not UTTmarks:	
		unit_two_marks = [1,1,1,1,2]
	else:
		unit_two_marks = UTTmarks
	if not UTTmarks:	
		unit_three_marks = [1,1,1,1,2]
	else:
		unit_three_marks = UTThmarks
	
	
#############	#############     ####################

def label_creator(data):
	"""creating y labels for bargraph"""
	label = []
	for i in data:
		b = str(i)+"/20"
		label.append(b)
	return label	
	
class RecordArea(Screen):
	stud_attend = student_attendance
	total_school_working_dy = total_school_working_day
	user_attendence_percentage = f"{stud_attend}"
	user_Result_analysis = "A+"
	Xvalues = [1,2,3,4,5]	
	Barlabel = ["Math","Cs","Physic","Chemistry","English"]
	ylabel = label_creator(unit_one_marks)
	print(label_creator(unit_one_marks))
	Yvalues = unit_one_marks
	print(unit_one_marks)
	def on_enter(self):
		chart_bar = self.ids.chart
		chart_bar.update()
	def menu_box(self):
		self.a = self.ids.drop_btn
		self.menu_items = [
			{
			"text": f"Term {i} marks",
			"viewclass": "OneLineListItem",
			"on_release": lambda x=f"Term {i} marks": self.menu_callback(x),
			} for i in range(1,4)
			]
		self.menu = MDDropdownMenu(
			caller=self.a,
			items=self.menu_items,
			position="auto",
			background_color=(1,1,1,1),
			opening_time=0,
			width_mult=4,
			)	
	def menu_callback(self, text_item):	
		def label_creator(data):
			"""creating y labels for bargraph"""
			label = []
			for i in data:
				b = str(i)+"/20"
				label.append(b)
			return label	
		self.menu.dismiss()
		self.ids.graph_title.text = f"{text_item}"
		list_text_item = text_item.split()
		chart_bar = self.ids.chart
		if int(list_text_item[1]) == 1:
			chart_bar.y_labels = label_creator(unit_one_marks)
			chart_bar.y_values = unit_one_marks
		elif int(list_text_item[1]) == 2:
			chart_bar.y_labels = label_creator(unit_two_marks)
			chart_bar.y_values = unit_two_marks
		
		elif int(list_text_item[1]) == 3:
			chart_bar.y_labels = label_creator(unit_three_marks)
			chart_bar.y_values = unit_three_marks
		else:
			pass
		chart_bar.update()