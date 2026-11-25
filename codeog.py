# import streamlit as st
import json

#st.set_page_config(page_title="Saket's Student Portal", page_icon="🎓", layout="centered")

# Step 1: Open and load the JSON file using encoding="utf-8" to prevent errors
with open("code.json", "r", encoding="utf-8") as file:
    students = json.load(file)

print("Welcome to Saket's Student Portal")
print("Instructions: Enter Students Full Name")
print("If you want to Filter students type Filter")

while True:
    wanted_student= input("Enter Student Name(or type Filter): ").lower().strip()
    existing_student = None

# 3. Loop through every student dictionary in your list
    for student in students:
    # Check if what was typed is inside the student's name
        if wanted_student in student["name"].lower():
            existing_student = student
            break
    if existing_student:
        print("STUDENT FOUND: ", existing_student["name"].upper())
        print("AGE:", existing_student["age"])
        print("GENDER:", existing_student["gender"].upper())
        print("HOBBIES:", ", ".join(existing_student["hobbies"]).upper())
        print("PERSONAL PROJECT:", existing_student["personal_project"].upper())
        print("FAVORITE SUBJECT:", existing_student["favorite_class"].upper(),"\n")
        print("GRADE IN PERSONAL PROJECT:", existing_student["grade"].upper()) #Accidentally put .upper() outside
        print("AFTER-SCHOOL CLUBS:", ", ".join(existing_student["clubs"]).upper())
        print("FAVORITE MUSIC ARTIST:", existing_student["music_artist"].upper())
        print("Two Truths and a Lie: ", existing_student["tnl"].upper())
        guess= input("Guess the lie(be sure to type it exactly as written): ").strip().lower()
        if guess== existing_student["lie"]:
            print("Correct! Great  Guess")
        else:
            print(f"Wrong, lie was {existing_student["lie"]}")
    elif wanted_student== "quit":
        print("Thanks for trying the program!")
        break
    elif wanted_student== "filter":
        filter=input("What would you like to filter by? (Options: Favorite Subject, Gender, Grade): ").lower().strip()
        a_grade=[]
        if filter== "grade":
            for student in students:
                if student["grade"]=="A" or student["grade"] == "A-":
                    a_grade.append(student)
            print(f"Number of students with A/A-(>89.5%): {len(a_grade)} ")
            for student in a_grade:
                print(student["name"])
            b_grade=[]
            for student in students:
                if student["grade"]=="B+":
                    b_grade.append(student)
            print(f"Number of students with B/B+(>86.5%)): {len(b_grade)} ")
            for student in b_grade:
                print(student["name"])
            not_available=[]
            for student in students:
                if student["grade"]=="n/a":
                    not_available.append(student)
            print(f"Number of students with grades not available: {len(not_available)} ")
            for student in not_available:
                print(student["name"])
        elif filter=="favorite subject":
            subjecto=input("Which Subject? (Science, Math, History, Music, Art, English): ").lower().strip()
            the_sub=[]
            for student in students:
                fav_class=student["favorite_class"]
                if subjecto in fav_class:
                    the_sub.append(student)
            print(f"Number of students who like {subjecto} :{len(the_sub)}")
            if the_sub: 
                for student in the_sub:
                    print(student["name"])
            else:
                print("Sorry no students found for that subject")
        elif filter== "gender":
            males=[]
            for student in students:
                if student["gender"]=="male":
                    males.append(student)
            print(f"Number of male students: {len(males)} ")
            for student in males:
                print(student["name"])
            females=[]
            for student in students:
                if student["gender"]=="female":
                    females.append(student)
            print(f"Number of female students: {len(females)} ")
            for student in females:
                print(student["name"])
        else:
            print("Filter not found.")
            print("Make sure filter is one of the options and spelt correctly")
    else:
        print("Sorry, Student not Found")

    # & "C:\Program Files\Python314\python.exe"-m streamlit run app.py  


