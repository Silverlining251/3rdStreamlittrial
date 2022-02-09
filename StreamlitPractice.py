# import module
import streamlit as st

#Display Images/Logos:

#Make sure you have saved the image into your jupyter folder containing your python script

#Display Images

#Import Image from pillow to open images
#Make sure you have installed the pillow package using your terminal/command line

#Import Image from pillow to open images
from PIL import Image
img = Image.open("shipping.png")
 
# display image using streamlit
# width is used to set the width of an image

st.image(img, width=500)

# Add Title

st.title("ThunderStruck Shipping Company of Nigeria")

#Always Save the python script
#Always Refresh your localhost now for the changes/new additions to appear

#Add Header and Sub-Header

# Header

st.header("Destination tracking App")
 
# Subheader

st.subheader("Track your Package")

#Add Text:
# Text

st.text("Enter package unique name")


# success

st.success("Success")



# title of the checkbox is 'Show/Hide' using the if conditional statement

if st.checkbox("Select/Unselect"):
    st.text("Selection Ready")

# display the text if the checkbox returns True value


#Radio Button:

# radio button
# first argument is the title of the radio button
# second argument is the options for the ratio button

status = st.radio("Select Location: ", ('Europe', 'Asia'))
 
# conditional statement to print
# Male if male is selected else print female
# show the result using the success function

if (status == 'Europe'):
    st.success("Europe")
else:
    st.success("Asia")             
             
#Selection Box:
#You can select any one option from the select box.
# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options

country = st.selectbox("Select Country: ",
                     ['Uk', 'France', 'Prague' 'China', 'India', 'Korea'])
 
###print the selected hobby

st.write("You have selected: ", country)


#Text Input:

# Text Input
 
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area

name = st.text_input("Enter Your name", "Type Here ...")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string


if(st.button('Submit')):
    result = name.title()
    st.success(result)

# Add Slider:

# slider
 
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number

level = st.slider("How Satisfied are you on a Scale of 5?", 1, 5)
 
# print the level
# format() is used to print value
# of a variable at a specific position

st.text('Selected: {}'.format(level))