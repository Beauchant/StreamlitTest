import base64
import time

import streamlit as st

st.title("Bienvenue!")
st.title("My first Streamlit App")
st.markdown("I'm very **happy** to learning **Streamlit** now.")

st.image("database1.png")
# st.image("Souris.png")

# --------------Widgets---------------
# Checkbox
st.checkbox("Pen")
st.checkbox("Pencil")

# Button
def btn():
    st.write("Button clicked!")


st.button("I'm a button", on_click=btn)

# RadioButton
sex = st.radio("Gender", ["Male", "Female"])
st.text(f"You are a {sex}")
country = st.radio("In which country do you live?", options=("UK", "USA", "Haiti"))

# Dropdown list (select box)
st.selectbox("(Select): Choose an option", ["Anglais", "Informatiques", "Math"])

# Multiselect
multiselect = st.multiselect("(Multiselect): Choose an option", ["Anglais", "Informatiques", "Math"])
st.write(multiselect)

# Slider
st.slider("(Slider): Choose your number", min_value=0, max_value=100)

# Select_slider
st.select_slider("(Select_slider): Rating", ["Bod", "Good", "Excellent", "Outstanding"])

# -------------Input--------------
nb1 = int(st.number_input("Entrez le nombre 1", 0))
nb2 = int(st.number_input("Entrez le nombre 2", 0))

result1 = nb1 + nb2
st.text(f"Le résultat de {nb1} + {nb2} est {result1}")

email = st.text_input("Enter your email")
st.write(f"Your email is: {email}")

# Date input
birthday = st.date_input("Enter your birthday")
st.write(f"Your birthday is: {birthday}")

# Time input
your_time = st.time_input("What time is it?")
st.write(f"It's {your_time}")

# Text area input
message = st.text_area("Write a comment")
st.write(message)

# File uploader
file = st.file_uploader("Choose your image", type=['.png', '.jpg', '.gif'], accept_multiple_files=True)
if file is not None:
    st.image(file)

video = st.file_uploader("Choose your video", type=['.mp4'])
if video is not None:
    st.video(video)

# Using color picker
pick = st.color_picker("Choose your color")

# Progress bar
st.progress(90)

# Spinner
with st.spinner("Wait..."):
    time.sleep(2)

# For celebration
st.balloons()

# Create sidebar
st.sidebar.title("My Sidebar")
em1 = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type="password")


def emp():
    st.sidebar.write(f"Email: {em1}, Password: {password}")


st.sidebar.button("Submit", on_click=emp)

# Jason
st.json({"name": "Bob, Martha, Toto", "age": "12, 14, 17"})
st.json({"name": ["Bob, Martha, Toto"], "age": ["12, 14, 17"]})

st.markdown("---")  # add a horizontal bar

code = """
# Using json format in Streamlit
st.json({"name": "Bob, Martha, Toto", "age": "12, 14, 17"})
st.json({"name": ["Bob, Martha, Toto"], "age": ["12, 14, 17"]})
"""

st.code(code, language="python")

# Using dataframe
import pandas as pd

st.write("## Students information")
student = pd.DataFrame({"Name": ["Boby", "Martine", "Phanor", "Martha"],
                        "Age": [21, 17, 19, 22],
                        "Sex": ["Male", "Female", "Male", "Female"]})
st.table(student)

st.write("## Products report")

products = ["Terminal", "Keyboard", "Mouse", "Box"]
unit_price = [105, 15, 7, 250]
quantity = [12, 10, 15, 10]
total = []

for i in range(4):
    total.append(unit_price[i] * quantity[i])

report = pd.DataFrame({"Products": products, "Unit_price $US": unit_price,
                       "Quantity": quantity, "Total": total})

st.dataframe(report)

# NB Using st.dataframe give us the possibility to resize and sort fields

# Working with medias
# 1- Display image
st.image("Computer.png")

# Display video
st.video("Disney.mp4")
# st.video("https://youtu.be/cUKqsnLGQBw?si=vAXV0PBtEwj2DwP0")

# Playing audio
st.audio("Best.aac")

st.markdown("""
<style>
            .css-6q9sum.ef3psqc3
            {
                visibility: hidden;
            }
            .css-cio0dv.ea3mdgi1
            {
                visibility: hidden;
            }
</style>
""", unsafe_allow_html=True)


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" ' \
                  f'type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


show_pdf('Lettre de motivation.pdf')
