import tkinter as tk 
import time 
from PIL import Image, ImageTk

# Main Application Window 
root= tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("500x500")

# List of Image Paths 
image_paths= [
    r"/Users/saumya/Desktop/Album/img0.jpeg",
    r"/Users/saumya/Desktop/Album/img1.JPG",
    r"/Users/saumya/Desktop/Album/img2.JPG",
    r"/Users/saumya/Desktop/Album/img3.jpeg",
    r"/Users/saumya/Desktop/Album/img4.jpg",
    r"/Users/saumya/Desktop/Album/img5.jpeg",
]

image_size= (700, 700)
images= []
for path in image_paths:
    img= Image.open(path)
    img= img.resize(image_size)
    images.append(img)  #Adding each image in the list

# Convert PIL Images into Tkinter Compatible Image 
final_images= []
for img in images:
    photo= ImageTk.PhotoImage(img) 
    final_images.append(photo)

# Label widget to keep photuuu 
image_label= tk.Label(root)
image_label.pack(pady=30)

# Slideshow Function 
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image= photo
        root.update()
        time.sleep(2)

#Button 
play_button= tk.Button(
    root,
    text= "Play the Slideshow",
    font=("Arial", 17),
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()



