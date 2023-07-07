import random
import string
from tkinter import *

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
            password = password + random.choice(characters)
    
    password_label.configure(text="Generated Password: " + password,font=("Times New Roman",20))

# Create the main root
root = Tk()
root.title("Password Generator")
# create the top header
length_label = Label(root, text="Password Generator",font=("Times New Roman",50),background="Blue")
length_label.pack(fill=BOTH)

# Create a label and entry for password length
length_label = Label(root, text="Password Length:",font=("Times New Roman",20))
length_label.pack()
length_entry = Entry(root)
length_entry.pack()

# Create a button to generate the password
generate_button = Button(root, text="Generate", command=generate_password,height=2,width=10,background="light Green")
generate_button.pack()

# Create a label to display the generated password
password_label = Label(root, text="Generated Password:",font=("Times New Roman",20))
password_label.pack()

root.mainloop()
