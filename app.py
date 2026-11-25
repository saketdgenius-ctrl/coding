import json
import streamlit as st

st.set_page_config(page_title="Saket's Student Portal", page_icon="🎓", layout="centered")

@st.cache_data
def load_students():
    with open("code.json", "r", encoding="utf-8") as file:
        return json.load(file)

try:
    students = load_students()
except FileNotFoundError:
    st.error("Error: 'code.json' was not found. Make sure it is in the same folder as app.py.")
    st.stop()

st.title("🎓 Saket's Student Portal")

# Visible tabs right on the main screen
tab1, tab2 = st.tabs(["🔍 Search Student", "📊 Filter Students"])

# --- TAB 1: SEARCH STUDENT ---
with tab1:
    wanted_student = st.text_input("Enter Student Name:").lower().strip()

    if wanted_student:
        existing_student = None
        for student in students:
            if wanted_student in student["name"].lower():
                existing_student = student
                break

        if existing_student:
            st.success(f"**STUDENT FOUND:** {existing_student['name'].upper()}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**AGE:** {existing_student['age']}")
                st.write(f"**GENDER:** {existing_student['gender'].upper()}")
                st.write(f"**FAVORITE SUBJECT:** {existing_student['favorite_class'].upper()}")
                st.write(f"**FAVORITE MUSIC ARTIST:** {existing_student['music_artist'].upper()}")
            
            with col2:
                st.write(f"**PERSONAL PROJECT:** {existing_student['personal_project'].upper()}")
                st.write(f"**PROJECT GRADE:** {existing_student['grade'].upper()}")
                st.write(f"**HOBBIES:** {', '.join(existing_student['hobbies']).upper()}")
                st.write(f"**AFTER-SCHOOL CLUBS:** {', '.join(existing_student['clubs']).upper()}")

            st.divider()

            st.subheader("🕵️ Two Truths and a Lie")
            st.info(existing_student["tnl"].upper())
            
            guess = st.text_input("Guess the lie (type it exactly as written):").strip().lower()
            
            if st.button("Submit Guess"):
                if guess == existing_student["lie"].strip().lower():
                    st.balloons()
                    st.success("Correct! Great Guess! 🎉")
                else:
                    st.error(f"Wrong! The lie was: **{existing_student['lie']}**")
        else:
            st.warning("Sorry, Student not Found.")

# --- TAB 2: FILTER STUDENTS ---
with tab2:
    filter_choice = st.selectbox(
        "What would you like to filter by?",
        ["Grade", "Favorite Subject", "Gender"]
    )

    if filter_choice == "Grade":
        a_grade = [s["name"] for s in students if s["grade"] in ["A", "A-"]]
        b_grade = [s["name"] for s in students if s["grade"] == "B+"]
        not_available = [s["name"] for s in students if s["grade"] == "n/a"]

        st.subheader(f"A / A- (>89.5%): {len(a_grade)} students")
        for name in a_grade:
            st.write(f"- {name}")

        st.subheader(f"B+ (>86.5%): {len(b_grade)} students")
        for name in b_grade:
            st.write(f"- {name}")

        st.subheader(f"Grades Not Available: {len(not_available)} students")
        for name in not_available:
            st.write(f"- {name}")

    elif filter_choice == "Favorite Subject":
        subject = st.selectbox(
            "Which Subject?",
            ["Science", "Math", "History", "Music", "Art", "English"]
        ).lower()

        the_sub = [s["name"] for s in students if subject in s["favorite_class"].lower()]
        
        st.subheader(f"Students who like {subject.capitalize()}: {len(the_sub)}")
        if the_sub:
            for name in the_sub:
                st.write(f"- {name}")
        else:
            st.info("Sorry, no students found for that subject.")

    elif filter_choice == "Gender":
        males = [s["name"] for s in students if s["gender"].lower() == "male"]
        females = [s["name"] for s in students if s["gender"].lower() == "female"]

        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"Male Students ({len(males)})")
            for name in males:
                st.write(f"- {name}")
        
        with col2:
            st.subheader(f"Female Students ({len(females)})")
            for name in females:
                st.write(f"- {name}")
