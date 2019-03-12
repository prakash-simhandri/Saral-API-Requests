import requests
import json
link='http://saral.navgurukul.org/api/courses'
calet_data=requests.get(link)
All_data=calet_data.json()
# print (All_data)
# with open("courses.json","w")as send:
# 	json.dump(All_data,send)

with open("courses.json","r")as open_file:
	data=json.load(open_file)
	# print (data)
	number = 1
	number_list=[]
	Id_list=[]
	# avail=All_data['availableCourses']
	for i in data:
		for j in data[i]:
			name_list=(number,j['name'])
			print(name_list)
			number_list.append(number)
			Id_list.append(j["id"])
			number+=1
		# print(number_list)
		print(Id_list)

user=int(input("Enter a number "))
for i in range(len(number_list)):
	if number_list[i] == user:
		a = (Id_list[user-1])
		# print("http://saral.navgurukul.org/api/courses/"+str(a)+"/exercises")
		link_1 = "http://saral.navgurukul.org/api/courses/"+str(a)+"/exercises"
		data_1 = requests.get(link_1)
		total_data=data_1.json()
		# print (total_data)
		number_2 = 1
		slug_list=[]
		slug_number = []
		for x in total_data:
			for z in total_data[x]:
				print (number_2,z["name"])
				slug_number.append(number_2)
				slug_list.append(z["slug"])
				# print(slug_list)
				number_2+=1
				w = z["childExercises"]
				for v in w:
					slug_list.append(v["slug"])
					slug_number.append(number_2)
					
					print("	",number_2,v["name"])
					number_2+=1
			# print(slug_number)
			# print (slug_list)

user_2=int(input("Enter the second number >"))
content=[]
slug=''
for new in range(len(slug_number)):
	if slug_number[new] == user_2:
			slug=slug_list[new]
			print (slug)
		# print("http://saral.navgurukul.org/api/courses/"+str(new)+"/exercise/getBySlug?slug=" + slug)
		
			link_2="http://saral.navgurukul.org/api/courses/"+str(new)+"/exercise/getBySlug?slug="+slug
			b = requests.get(link_2)
			Cdata = b.json()
			print(Cdata["content"])
		


# second API in crieat in funchan---------------------------------------





# import requests
# import json

# def course_name():
# 	var = requests.get("http://saral.navgurukul.org/api/courses")
# 	data = var.json()
# 	# print(data)
# 	number = 1
# 	for i in data:
# 		for j in data[i]:
# 			print(number,j["name"])
# 			number+=1
# course_name()

# def id_find():
# 	var = requests.get("http://saral.navgurukul.org/api/courses")
# 	data = var.json()
# 	id_list = []
# 	for i in data:
# 		for j in data[i]:
# 			id_list.append(j["id"])
# 	return id_list
# print(id_find())
		
# print('')
# user_1 = int(input("any number you want chek course "))

# def menu_list(user):
# 	a=id_find()
# 	# print(len(a))
# 	number_list = []
# 	b=len(a)
# 	for i in range(1,b+1):
# 		number_list.append(i)
# 	# print(number_list)

# 	for i in number_list:
# 		if i == user:
# 			# print(i)
# 			y=a[i-1]
# 			# print(y)
# 			link_id = requests.get(" http://saral.navgurukul.org/api/courses/"+str(y)+"/exercises")
# 			sec_data = link_id.json()
# 			# print(sec_data)

# 			for i in sec_data:
# 				number=1
# 				for j in sec_data[i]:
# 					print(number,j["name"])
# 					number+=1
# 					a=j["childExercises"]
# 					for k in a:
# 						print('	',number,k["name"])
# 						number+=1
# menu_list(user_1)


# def slug_menu_list(user):
# 	list_slug = []
# 	a=id_find()
# 	# print(len(a))
# 	number_list = []
# 	b=len(a)
# 	for i in range(1,b+1):
# 		number_list.append(i)
# 	# print(number_list)

# 	for i in number_list:
# 		if i == user:
# 			# print(i)
# 			y=a[i-1]
# 			# print(y)
# 			link_id = requests.get(" http://saral.navgurukul.org/api/courses/"+str(y)+"/exercises")
# 			sec_data = link_id.json()
# 			# print(sec_data)

# 			for i in sec_data:
# 				number=1
# 				for j in sec_data[i]:
# 					list_slug.append(number)
# 					list_slug.append(j["slug"])
# 					number+=1
# 					a=j["childExercises"]
# 					for k in a:
# 						list_slug.append(number)
# 						list_slug.append(k["slug"])
# 						number+=1
# 	return(list_slug)
# print(slug_menu_list(user_1))

# def content_find(user,choice):
# 	list_slug = []
# 	a=id_find()
# 	# print(len(a))
# 	number_list = []
# 	b=len(a)
# 	for i in range(1,b+1):
# 		number_list.append(i)
# 	# print(number_list)

# 	for i in number_list:
# 		if i == user:
# 			y=a[i-1]
# 			# print(y)

# 	find_slug = slug_menu_list(user_1)
# 	# print(find_slug)
# 	print('')
# 	# chouse = int(input("input any number you want open content "))
# 	print('')
# 	for i in range(len(find_slug)):
# 		if choice == find_slug[i]:
# 			# print(find_slug[i+1])
# 			new_var= requests.get("http://saral.navgurukul.org/api/courses/"+str(y)+"/exercise/getBySlug?slug="+find_slug[i+1])
# 			third_data = new_var.json()
# 			# print(third_data)
# 			print(third_data["content"])
# content_find(user_1,int(input("input any number you want open content ")))



# course_name()
# print('')
# user_1 = int(input("any number you want chek course "))
# m=user_1
# menu_list(user_1)
# print('')
# user_5=int(input("input any number you want open content "))
# content_find(user_1,user_5)

# Next=user_5
# while True:
# 	print('')
# 	user_3 = input("input/ up=agen_corse/ n=Next/ p=previous/ b=break ")
# 	if user_3 == "up" or user_3 == "UP":
# 		course_name()
# 		print('')
# 		user_1 = int(input("any number you want chek course "))
# 		print('')
# 		menu_list(user_1)
# 		print('')
# 		user_5=int(input("input any number you want open content "))
# 		content_find(user_1,user_5)
	
# 	elif user_3 == "n" or user_3 == "N":
# 		content_find(m,Next+1)
# 		Next+=1

# 	elif user_3 == "p" or user_3 == "P":
# 		content_find(m,Next-1)
# 		Next-=1
# 	else:
# 		break