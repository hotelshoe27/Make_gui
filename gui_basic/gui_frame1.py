from tkinter import*

root = Tk()
root.title("frog")
root.geometry("640x480+500+100")

photo = photoImage(file="gui_basic/btn1.png")
btn1 = Button(root, image=photo)
btn1.pack()

root = mainloop()