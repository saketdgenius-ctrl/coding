import streamlit as st
#all i do is replace print with st.write and input with st.text_input
import json

st.set_page_config(page_title="Saket's Student Portal", page_icon="🎓", layout="centered")

# Step 1: Open and load the JSON file using encoding="utf-8" to prevent errors
with open("code.json", "r", encoding="utf-8") as file:
    students = json.load(file)

st.write("Welcome to Saket's Student Portal")
st.write("Instructions: ") 
st.write("-Enter Students Full Name to Learn About Them")
st.write("-If you want to Filter students type Filter")
st.write("-To stop the program type quit")

wanted_student = st.text_input("                    ").lower().strip()
                                #Enter Student Name(or type Filter):Removed this because i already gave instructions

if wanted_student:
    existing_student = None

    # 3. Loop through every student dictionary in your list
    for student in students:
        # Check if what was typed is inside the student's name
        if wanted_student in student["name"].lower():
            existing_student = student
            break

    if existing_student:
        st.write("STUDENT FOUND: ", existing_student["name"].upper())
        st.write("AGE:", existing_student["age"])
        st.write("GENDER:", existing_student["gender"].upper())
        st.write("HOBBIES:", ", ".join(existing_student["hobbies"]).upper())
        st.write("PERSONAL PROJECT:", existing_student["personal_project"].upper())
        st.write("FAVORITE SUBJECT:", existing_student["favorite_class"].upper())
        st.write("GRADE IN PERSONAL PROJECT:", existing_student["grade"].upper()) #Accidentally put .upper() outside
        st.write("AFTER-SCHOOL CLUBS:", ", ".join(existing_student["clubs"]).upper())
        st.write("FAVORITE MUSIC ARTIST:", existing_student["music_artist"].upper())
        st.write("--------------------------")
        st.write("Mini-Game")
        st.write("Two Truths and a Lie: ", existing_student["tnl"].upper())
        
        guess = st.text_input("Guess the lie(be sure to type it exactly as written): ").strip().lower()
        if guess:
            if guess == existing_student["lie"]:
                st.write("Correct! Great  Guess")
            else:
                st.write(f"Wrong, lie was {existing_student['lie']}")

    elif wanted_student == "quit":
        st.write("Thanks for trying the program!")

    elif wanted_student == "filter":
        filter = st.text_input("What would you like to filter by? (Options: Favorite Subject, Gender, Grade): ").lower().strip()
        a_grade = []
        
        if filter == "grade":
            for student in students:
                if student["grade"] == "A" or student["grade"] == "A-":
                    a_grade.append(student)
            st.write(f"Number of students with A/A-(>89.5%): {len(a_grade)} ")
            for student in a_grade:
                st.write(student["name"])
                
            b_grade = []
            for student in students:
                if student["grade"] == "B+":
                    b_grade.append(student)
            st.write(f"Number of students with B/B+(>86.5%)): {len(b_grade)} ")
            for student in b_grade:
                st.write(student["name"])
                
            not_available = []
            for student in students:
                if student["grade"] == "n/a":
                    not_available.append(student)
            st.write(f"Number of students with grades not available: {len(not_available)} ")
            for student in not_available:
                st.write(student["name"])

        elif filter == "favorite subject":
            subjecto = st.text_input("Which Subject? (Science, Math, History, Music, Art, English): ").lower().strip()
            if subjecto:
                the_sub = []
                for student in students:
                    fav_class = student["favorite_class"]
                    if subjecto in fav_class:
                        the_sub.append(student)
                st.write(f"Number of students who like {subjecto}: {len(the_sub)}")
                if the_sub: 
                    for student in the_sub:
                        st.write(student["name"])
                else:
                    st.write("Sorry no students found for that subject")

        elif filter == "gender":
            males = []
            for student in students:
                if student["gender"] == "male":
                    males.append(student)
            st.write(f"Number of male students: {len(males)} ")
            for student in males:
                st.write(student["name"])
                
            females = []
            for student in students:
                if student["gender"] == "female":
                    females.append(student)
            st.write(f"Number of female students: {len(females)} ")
            for student in females:
                st.write(student["name"])

        elif filter != "":
            st.write("Filter not found.")
            st.write("Make sure filter is one of the options and spelt correctly")

    else:
        st.write("Sorry, Student not Found")

    #& "C:\Program Files\Python314\python.exe" -m streamlit run code.py 
    #required to run