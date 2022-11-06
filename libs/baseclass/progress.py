from kivy.uix.screenmanager import Screen
import datetime
from Modules.db import months
#m,cs,p,c,e
unit_one_marks = [1,2,1,2,1]
unit_two_marks = [1,2,1,2,1]
unit_three_marks = [1,2,1,2,1]
total_school_working_day = 88
with open("Modules//loginfo.txt","r+") as f:
	logged = f.read().split(",")
	student_attendance = logged[len(logged)-1]
with open("Modules//numbers.txt","r+") as f:
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
	unit_one_marks = UTOmarks
	unit_two_marks = UTTmarks
	unit_three_marks = UTThmarks
class Progress_Screen(Screen):
	def percentage_calc_ut(marks):
		mark = sum(marks)
		return round(mark/100*100,2)
	unit1_marks_percent = f"{percentage_calc_ut(unit_one_marks)}%"
	unit2_marks_percent = f"{percentage_calc_ut(unit_two_marks)}%"
	unit3_marks_percent  = f"{percentage_calc_ut(unit_three_marks)}%"
	def update_test_records(self):
		self.ids.Unit1_percent_marks.text = self.unit1_marks_percent
		self.ids.Unit2_percent_marks.text = self.unit2_marks_percent 
		self.ids.Unit3_percent_marks.text = self.unit3_marks_percent 
		self.ids.Halfyearly_percent_marks
		self.ids.Final_percent_marks
	def on_enter(self):
		self.update_test_records()
	date = str(datetime.date.today())
	b = int(date[5:7])
	marks = [0,20,20,20,20,20,20,20,18,20,19,16]
	y_labels_algo = []
	for i in marks:
		if i > 18 and i<20:
			y_labels_algo.append("A")
		elif i==20:
			y_labels_algo.append("A+")
		elif i<18 and i>14:
			y_labels_algo.append("B+")
		elif i<14 and i>10:
			y_labels_algo.append("B")
		elif i<10 and i>7:
			y_labels_algo.append("C")
		else:
			y_labels_algo.append(" ")
	student_progressvalue = marks
	
	def update_line_chart(self):
		"""method to update the line chart value in progress screen."""
		chart1 = self.ids.chart1
		chart1.x_values = [x for x in range(self.b+1)]
		print(self.b)
		chart1.y_values = self.marks
		chart1.x_labels = months[0:self.b+1]
		chart1.y_labels= self.y_labels_algo
		chart1.update()