UTOmarks = []
with open("numbers.txt","r+") as f:
	a = f.read().split("-")
	b = a[0].replace("["," ")
	c = b.replace("]"," ").replace("'","").split(",")
	for item in c:
		UTOmarks.append(int(item.strip()))

print(UTOmarks)