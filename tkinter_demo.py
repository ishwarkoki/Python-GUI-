from tkinter import *  # importing Tkinter library -> builtin py lib
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email=email_input.get()
    password=pass_input.get()
    if email == 'ishwarkoki@gmail.com' and password== 'Amma':
        messagebox.showinfo("yay! Login Successful")
    else:
        messagebox.showerror("Error, login Unsuccessful")

root = Tk()

root.title('Login window')
root.iconbitmap('python.ico')
root.geometry('350x500')
root.configure(background='#0096DC')

img = Image.open('icon.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

#labels -->
img_label = Label(root,image=img,bg='#0096DC')
img_label.pack(pady=(10,10))

text_label = Label(root, text = "Python Store",fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

# for Email entry Box -->
email_label= Label(root,text="enter your email",fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input= Entry(root,width=50)
email_input.pack(ipady=5,pady=(1,15))

# For password entry box -->

pass_label= Label(root,text="enter your password",fg='white',bg='#0096DC')
pass_label.pack(pady=(20,5))
pass_label.config(font=('verdana',12))

pass_input= Entry(root,width=50)
pass_input.pack(ipady=5,pady=(10,15))

# For login button -->

login_btn= Button(root,text="login",bg='white',fg='black',command=handle_login)
# For functionality - command Attribute = some_function.
login_btn.pack(pady=(10,20))
login_btn.config(font =('verdana'),width=20)


root.mainloop()