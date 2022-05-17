from tkinter import *
from PIL import ImageTk, Image
import os

# rotate func rotate the Images in the directory One by One --> 
def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])  # Image label is used to pack on root
    # Img_array is used here which has all the Images stored in it
    counter+=1

counter=1
root=Tk()
root.title("wallpaper-Viewer")
root.iconbitmap('wall_icon.ico')
root.geometry('300x450')
root.config(bg ='black')


# Reading the directory which has images --> wallpaper
# Os module is used, using a loop all the images are being stored in an array

files=os.listdir(path='wallpaper')
img_array=[]
for file in files:
    img = Image.open(os.path.join('wallpaper', file))
    img_resized = img.resize((200, 300))
    img_array.append(ImageTk.PhotoImage(img_resized))

# Image label is created which is being packed on the root -->
img_label= Label(root,image=img_array[0])
img_label.config(bg='black')
img_label.pack(pady =(30,10))

# Next button is created with a function/command --> rotate Image.
next_btn=Button(root,text="Next",bg= 'white',fg ='black',width=28, height=2,command=rotate_img)
next_btn.pack(pady=(15,5)) 

root.mainloop()