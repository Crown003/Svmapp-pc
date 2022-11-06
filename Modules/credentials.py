id = 26
password =  "Crown03"
hashword = []
for i in password:
	hashword.append(str(ord(i)+id))
#print(type(ord("C")))
def decoder(id,passwd):
	main_pass = ""
	for i in hashword:
		main_pass += str(chr(int(i)-id))
	return main_pass
