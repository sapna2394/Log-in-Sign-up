
import json
user=input("Enter whether you want to log in or sign up:")
f=open("userdetails.json","r+")
name=f.read()
list3=[]
main_list=[]
dic={}
if user=="sign up":
    username=input("Enter your username:")
    password1=input("Enter your password:")
    password2=input("confirm your password:")
    if password1!=password2:
        print("Both passwords are not same!!")
    if "#" or "@" in password2 and password1:
        print("Password is confirmed")
    else:
        print("Atleast one special should contain one special character!")        
    list1=["Username","Password"]
    list2=[username,password2]
    i=0
    while i<=1:
        list3.append((list1[i],list2[i]))
        i+=1
    dic.update(list3)
    if username in name:
        print("Sorry! Your username already exist.")
    else:
        main_list.append(dic)
        print("congrats!! "+username+" you are signed up successfully.")
        print("Now you need to fill the following details:")
        description=input("Enter your desciption:")
        date_of_birth=input("Enter your date of birth:")
        hobbies=input("Enter your hobby:")
        gender=input("Enter your gender:")
        list4=["description","date of birth","hobbies","gender"]
        list5=[description,date_of_birth,hobbies,gender]
        j=0
        while j<len(list4):
            list3.append((list4[j],list5[j]))
            j+=1
        dic.update(list3)
        final_dic={}
        final_list=[]
        final_list.append(("user",dic))
        final_dic.update(final_list)
        json.dump(final_dic,f,indent=2)
if user=="log in":
    username=input("Enter your username:")
    password=input("Enter your password:")
    if username in name:
        print("congrats!! "+username+" you are logged in successfully.")
        print("Here are your details:")
        with open("userdetails.json") as f:
            x=json.load(f)
            for z in x.values():
                for u in z:
                    print(u,":",z[u])
    else:
        print("Invalid username and password")