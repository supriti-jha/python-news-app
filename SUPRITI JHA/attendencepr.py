# # import tkinter as tk
# # root = tk.Tk()

# # # root window title and dimension
# # root.title("STUDENTS ATTENDENCE ✔")
# # # Set geometry (widthxheight)
# # root.geometry('500x500')




# # root.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# # Function to validate the login
# def validate_login():
#     userid = username_entry.get()
#     password = password_entry.get()

#     # You can add your own validation logic here
#     if userid == "supriti" and password == "123456789":
#         messagebox.showinfo("Welcome, Admin", "Login Successful ✔")
#     else:
#         messagebox.showerror("Login Failed", "Invalid username or password")

# # Create the main window
# parent = tk.Tk()
# parent.title("Login Form")

# # Create and place the username label and entry
# username_label = tk.Label(parent, text="Userid:")
# username_label.pack()

# username_entry = tk.Entry(parent)
# username_entry.pack()

# # Create and place the password label and entry
# password_label = tk.Label(parent, text="Password:")
# password_label.pack()

# password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
# password_entry.pack()

# # Create and place the login button
# login_button = tk.Button(parent, text="Login", command=validate_login)
# login_button.pack()


# # Start the Tkinter event loop
# parent.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# def registration():
#     userid = username_entry.get()
#     password = password_entry.get()

#     # You can add your own validation logic here
#     if __name__ == "supriti" and emailentry == "supriti@gmail.com" and password == "123456789" and phonenoentry == "123456789":
#         messagebox.showinfo("Welcome Admin", "register Successfully ✔")
#     else:
#         messagebox.showerror("Login Failed", "Invalid name or password")

# # Create the main window
# parent = tk.Tk()
# parent.title("Registration Form")

# # Create and place the username label and entry
# namelabel = tk.Label(parent, text="name:")
# namelabel.pack()

# nameentry = tk.Entry(parent)
# nameentry.pack()

# # Create and place the password label and entry
# emaillabel = tk.Label(parent, text="email:")
# emaillabel.pack()

# emailentry = tk.Entry(parent)  # Show asterisks for password
# emailentry.pack()

# passwordlabel = tk.Label(parent, text="password:")
# passwordlabel.pack()

# passwordentry = tk.Entry(parent,show="*")  # Show asterisks for password
# passwordentry.pack()

# phonenolabel = tk.Label(parent, text="phoneno:")
# phonenolabel.pack()

# phonenoentry = tk.Entry(parent, show="*")  # Show asterisks for password
# phonenoentry.pack()

# # Create and place the login button
# login_button = tk.Button(parent, text="Registration", command=registration)
# login_button.pack()

# parent.mainloop()

import tkinter as tk
from tkinter import messagebox


# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    # You can add your own validation logic here
    if userid == "supriti" and password == "123456789":
        messagebox.showinfo("Welcome, Admin", "Login Successful ✔")
        show_registration_form()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to show the registration form
def show_registration_form():
    login_frame.pack_forget()  # Hide the login form
    registration_frame.pack(pady=20)  # Show the registration form

# Function to handle registration
def registration():
    name = nameentry.get()
    email = emailentry.get()
    password = passwordentry.get()
    phoneno = phonenoentry.get()

    # Registration logic, for example, checking if the fields are filled correctly
    if name == "supriti" and email == "supriti@gmail.com" and password == "123456789" and phoneno == "123456789":
        messagebox.showinfo("Registration Successful", "You have registered successfully ✔")
    else:
        messagebox.showerror("Registration Failed", "Invalid information entered")

# Create the main window
parent = tk.Tk()
parent.title("Login")

# Create the login form frame
login_frame = tk.Frame(parent)

# Create and place the username label and entry
username_label = tk.Label(login_frame, text="Userid:")
username_label.pack()

username_entry = tk.Entry(login_frame)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(login_frame, text="Password:")
password_label.pack()

password_entry = tk.Entry(login_frame, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(login_frame, text="Login", command=validate_login)
login_button.pack()

# Create the register button to switch to the registration form
register_button = tk.Button(login_frame, text="Register", command=show_registration_form)
register_button.pack()

login_frame.pack(pady=20)  # Initially show the login form

# Create the registration form frame
registration_frame = tk.Frame(parent)

# Create and place the name label and entry
namelabel = tk.Label(registration_frame, text="Name:")
namelabel.pack()

nameentry = tk.Entry(registration_frame)
nameentry.pack()

# Create and place the email label and entry
emaillabel = tk.Label(registration_frame, text="Email:")
emaillabel.pack()

emailentry = tk.Entry(registration_frame)
emailentry.pack()

# Create and place the password label and entry
passwordlabel = tk.Label(registration_frame, text="Password:")
passwordlabel.pack()

passwordentry = tk.Entry(registration_frame, show="*")
passwordentry.pack()

# Create and place the phone number label and entry
phonenolabel = tk.Label(registration_frame, text="Phone Number:")
phonenolabel.pack()

phonenoentry = tk.Entry(registration_frame)
phonenoentry.pack()

# Create and place the registration button
register_button_form = tk.Button(registration_frame, text="Register", command=registration)
register_button_form.pack()


# Start the Tkinter event loop
parent.mainloop()




