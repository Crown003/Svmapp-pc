from kivy.uix.screenmanager import Screen
import datetime
from Modules.db import months
import json
#maths,cs,physic,chemistry,english
unit_one_marks = [1,2,1,2,1]
unit_two_marks = [1,2,1,2,1]
unit_three_marks = [1,2,1,2,1]
total_school_working_day = 88
with open("Modules//loginfo.json","r+") as f:
	logged = json.loads(f.read())
unit_one_marks = logged["userMarks"]["UnitOneMarks"]
unit_two_marks =  logged["userMarks"]["UnitTwoMarks"]
unit_three_marks =  logged["userMarks"]["UnitThreeMarks"]

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