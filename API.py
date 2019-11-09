import requests
import json
from os import path

if True != path.exists("courses.json"):
	link = "http://saral.navgurukul.org/api/courses"
	data = requests.get(link)
	courses_data = data.json() # this lien convert to dict
	with open("courses.json","w") as open_file:
		json.dump(courses_data,open_file) 
		print(courses_data)
else:
	with open("courses.json","r") as open_file:
		open_All_data =json.load(open_file)
		numbering = 1
		Id_list=[]
		for courses_list in open_All_data["availableCourses"]:
			Id_list.append(courses_list["id"])
			print(numbering ,">>",courses_list["name"],"\n",{'Description':courses_list["shortDescription"]})
			print("\n")
			numbering+=1


		user_choice = int(input("Which courses you want >> "))
		print(" ")
		exercises_data = requests.get("http://saral.navgurukul.org/api/courses/"+str(Id_list[user_choice-1])+"/exercises")
		exercises_data = exercises_data.json()
		numbering = 1 
		slug_list=[]
		for exercise_list in exercises_data["data"]:
			print(numbering,">>",exercise_list["name"])
			slug_list.append(exercise_list["slug"])
			numbering+=1



		user_second_choice=int(input("Which slug you want >>"))
		print(" ")
		exercise_id = Id_list[user_choice-1]
		slug_name = slug_list[user_second_choice-1]
		slug_url='http://saral.navgurukul.org/api/courses/{}/exercise/getBySlug?slug={}'.format(exercise_id,slug_name)
		slug_data=requests.get(slug_url)
		slug_data=slug_data.json()
		print(slug_data["content"])

