edit=int(input("1.Edit Specific Line" +"\n"+ "2.Add New Line "+"\n"+"3.View Data's "+"\n"+"Enter Your Option : "))
if edit==1:
	with open('/home/pi/PYTHON/file_handling/stats.txt', 'r') as file:
		data = file.readlines()
	print (data)

	content_number=int(input("Enter Your Content Number :"))
	text=input("Enter Your Text: ")

	print ("Your name: " + data[0])
	data[content_number] = str(text+"\n")

	with open('/home/pi/PYTHON/file_handling/stats.txt', 'w') as file:
		file.writelines( data )
elif edit==2:
	text=input("Enter Your Text: ")
	data = ("\n"+(str(text)))

	with open('/home/pi/PYTHON/file_handling/stats.txt', 'a') as file:
		file.writelines( data )

elif edit==3:
	with open('/home/pi/PYTHON/file_handling/stats.txt', 'r') as file:
		data = file.readlines()
	print (data)

else:
	print("Something Problem")
