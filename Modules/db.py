import pymongo
from .credentials import hashword,id,decoder
import gridfs
from kivy.utils import platform
from os import getcwd as cwd
try:
	client = pymongo.MongoClient("mongodb://"+decoder(id,hashword)+":Crown@cluster0-shard-00-00.ltvt2.mongodb.net:27017,cluster0-shard-00-01.ltvt2.mongodb.net:27017,cluster0-shard-00-02.ltvt2.mongodb.net:27017/Main?ssl=true&replicaSet=atlas-he2q4w-shard-0&authSource=admin&retryWrites=true&w=majority")
	db = client["Main"]
	collection = db["UserData"]
except:
	print("Unable to connect the server.")
print(cwd)			


months = ["","jan","feb","mar","apr","may","jun","jul",
					"aug","sep","oct","nov","dec"]


#Lectures chapter list #
p = ["Electric Charges and Fields",
			"Electric Potential Difference",
			"Current Electricity",
			"Moving Charges and Magnetism",
			"Magnetism and Matter",
			"Electromagnetic Induction",
			"Alternating Current",
			"Electromagnetic Waves",
			"Ray Optics and Optical Instruments",
			"Wave Optics",
			"Dual Nature of Radiation and Matter",
			"Atoms",
			"Nuclei",
			"Semiconductor Electronics",
			"Communication Systems",]
			
m = ["Relations & Functions",
			"Inverse Trignometry and Functions",
			"Matrices",
			"Determinants",
			"Continuity and Differentiability",
			"Application of Derivatives",
			"Integrals",
			"Application of Integrals",
			"Differential Equations",
			"Vector Algebra",
			"Three Dimensional Geometry",
			"Linear Programming",
			"Probability",
			]
c = ["Solid State","Solution","Electrochemistry"
			,"Chemical Kinetics"
			,"Surface Chemistry"
			,"General Principles and Processes of Isolation of Elements"
			"The p-Block Elements"
			,"Chapter 8: The d & f Block Elements"
			,"Coordination Compounds"
			,"Haloalkanes and Haloarenes"
			,"Alcohols, Phenols, and Ethers"
			,"Aldehydes, Ketones, and Carboxylic Acids"
			,"Amines"
			,"Biomolecules"
			,"Polymers"
			,"Chemistry in Everyday Life",]
			
cs= ["REVIEW OF PYTHON – I",
			"REVIEW OF PYTHON – II",
			"WORKING WITH FUNCTIONS",
			"USING PYTHON LIBRARIES",	
			"FILE HANDLING",
			"RECURSION",
			"IDEA OF ALGORITHMIC EFFICIENCY",
			"DATA VISUALIZATION",
			"DATA STRUCTURES – I",
			"DATA STRUCTURES – II",
			"COMPUTER NETWORKS – I",
			"COMPUTER NETWORKS – II",
			"MySQL: SQL REVISION TOUR",
			"MORE ON SQL",
			"CREATING A DJANGO BASED BASIC WEB APPLICATION",
			"INTERFACE PYTHON WITH MySQL",
			"SOCIETY, LAW, AND ETHICS",]


#name_of_file = "Chapter2.pdf"
#file_location = "/storage/emulated/0/svmapp/Notes/Physics/" + name_of_file
#file_data = open(file_location,"rb")
#data = file_data.read()
#file_data.close()

#def upload_file():
#	fs.put(data, filename = name_of_file)
#	print("upload completed.")
#upload_file()

fs = gridfs.GridFS(db)
def download_file(name_of_file):
		data = db.fs.files.find_one({"filename":name_of_file+".pdf"})
		my_id = data["_id"]
		chunksize = data["chunkSize"]
		print((chunksize/1024)/1024 ,"mb")
		outputdata = fs.get(my_id).read()
		if platform != "android":
			download_location = cwd()+"\\Notes\\" + name_of_file + ".pdf"
		else:
			download_location = "/storage/emulated/0/MyApp/Notes/"+ name_of_file + ".pdf"	
		
		output = open(download_location,"wb+")
		output.write(outputdata)
		output.close()
